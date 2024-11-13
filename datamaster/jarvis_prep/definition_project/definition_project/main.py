import sys

from delta.tables import DeltaTable
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    cast,
    col,
    desc,
    explode,
    from_json,
    row_number,
)
from pyspark.sql.types import (
    ArrayType,
    IntegerType,
    StringType,
    StructField,
    StructType,
)
from pyspark.sql.window import Window


def foreach_batch_function(ds, batch_id):
    print(f'Processing batch {batch_id}')

    # Define a janela de partição para ordenar os dados
    windowSpec = Window.partitionBy('user_id', 'tipo_id').orderBy(
        desc('EnqueuedTimeUtc')
    )

    # Seleciona a linha mais recente para cada combinação de user_id e tipo_id
    new_df = (
        ds.select(
            explode(from_json(col('body').cast(StringType()), schema)).alias(
                'test'
            ),
            col('EnqueuedTimeUtc'),
        )
        .select(
            col('test.user_id').alias('user_id'),
            col('test.tipo_id').alias('tipo_id'),
            col('test.tipo_dados').alias('tipo_dados'),
            col('test.status').alias('status'),
            col('test.plataforma_origem').alias('plataforma_origem'),
            col('EnqueuedTimeUtc'),
        )
        .withColumn('RN', row_number().over(windowSpec))
        .where('RN == 1')
    )

    table_name = 'crisk.silver.consents'
    delta_table = DeltaTable.forName(
        SparkSession.builder.getOrCreate(), table_name
    )

    print(f'Performing merge (upsert) for batch {batch_id}')

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

    print(f'Batch {batch_id} processed successfully')


def main():
    print('Starting the data processing job')

    # Define o esquema dos dados
    schema = ArrayType(
        StructType(
            [
                StructField('user_id', IntegerType(), nullable=False),
                StructField('tipo_id', StringType(), nullable=False),
                StructField('tipo_dados', StringType(), nullable=False),
                StructField('status', StringType(), nullable=False),
                StructField('plataforma_origem', StringType(), nullable=True),
            ]
        )
    )

    table_name = 'crisk.silver.consents'
    logins_checkpoint = (
        '/Volumes/crisk/silver/volume_checkpoint_locations_silver/consents'
    )

    print('Reading data from the source table')

    # Leitura dos dados em modo batch
    (
        SparkSession.builder.getOrCreate()
        .readStream.format('delta')
        # .option('ignoreChanges', 'true')
        .table('crisk.bronze.consents')
        .writeStream.trigger(availableNow=True)
        .option('checkpointLocation', logins_checkpoint)
        .foreachBatch(foreach_batch_function)
        .start()
        .awaitTermination()
    )

    print('Data processing job completed successfully')
    print('Merge operation completed successfully')


def hello_world():
    print('hello world')


if __name__ == '__main__':
    main()
