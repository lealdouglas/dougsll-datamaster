import sys

from delta.tables import DeltaTable
from pyspark.sql import SparkSession
from pyspark.sql.functions import cast, col, explode, from_json
from pyspark.sql.types import IntegerType, StringType, StructField, StructType


def merge_silver(spark, new_df, table_name):

    # Carrega a tabela Delta
    delta_table = DeltaTable.forName(spark, table_name)

    # Realiza o merge (upsert) dos dados novos na tabela Delta
    delta_table.alias('target').merge(
        new_df.alias('source'),
        'target.user_id = source.user_id and target.tipo_id = source.tipo_id',
    ).whenMatchedUpdate(
        set={
            'status': 'source.status',
            'plataforma_origem': 'source.plataforma_origem',
        }
    ).whenNotMatchedInsert(
        values={
            'user_id': 'source.user_id',
            'tipo_id': 'source.tipo_id',
            'tipo_dados': 'source.tipo_dados',
            'status': 'source.status',
            'plataforma_origem': 'source.plataforma_origem',
        }
    ).execute()

    print('Merge realizado com sucesso!')


def main():

    schema = StructType(
        [
            StructField(
                'user_id',
                IntegerType(),
                nullable=False,
            ),
            StructField(
                'tipo_id',
                StringType(),
                nullable=False,
            ),
            StructField(
                'tipo_dados',
                StringType(),
                nullable=False,
            ),
            StructField(
                'status',
                StringType(),
                nullable=False,
            ),
            StructField('plataforma_origem', StringType(), nullable=True),
        ]
    )

    table_name = 'crisk.silver.consents'

    # Inicializa a SparkSession com suporte ao Delta Lake
    spark = SparkSession.builder.getOrCreate()

    # Leitura dos dados em modo batch
    new_df = (
        spark.read.format('delta')
        .table('crisk.bronze.consents')
        .select(
            from_json(col('body').cast(StringType()), schema).alias('test')
        )
        .select(
            col('test.user_id').alias('user_id'),
            col('test.tipo_id').alias('tipo_id'),
            col('test.tipo_dados').alias('tipo_dados'),
            col('test.status').alias('status'),
            col('test.plataforma_origem').alias('plataforma_origem'),
        )
    )

    # merge bronze com dados existentes na tabela silver
    merge_silver(spark, new_df, table_name)

    print('Processo finalizado com sucesso!')


def hello_world():
    print('hello world')


if __name__ == '__main__':
    main()
