from pyspark.sql import SparkSession
from delta.tables import DeltaTable


def merge_silver(spark, new_df):

    # Nome da tabela Delta
    table_name = 'crisk.silver.account'

    # Carrega a tabela Delta
    delta_table = DeltaTable.forName(spark, table_name)

    # Realiza o merge (upsert) dos dados novos na tabela Delta
    delta_table.alias('target').merge(
        new_df.alias('source'), 'target.user_id = source.user_id'
    ).whenMatchedUpdate(
        set={
            'name': 'source.name',
            'email': 'source.email',
            'city': 'source.city',
        }
    ).whenNotMatchedInsert(
        values={
            'user_id': 'source.user_id',
            'name': 'source.name',
            'email': 'source.email',
            'city': 'source.city',
        }
    ).execute()


def main():

    # Inicializa a SparkSession com suporte ao Delta Lake
    spark = SparkSession.builder.getOrCreate()

    # Leitura dos dados em modo batch
    new_df = spark.read.format('delta').table('crisk.bronze.account')

    # merge bronze com dados existentes na tabela silver
    merge_silver(spark, new_df)

    # Exibe os dados atualizados
    updated_df = spark.table(table_name).filter('user_id = 1234567890')
    updated_df.show()


def hello_world():
    print('hello world')
