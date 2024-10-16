import sys

from delta.tables import DeltaTable
from pyspark.sql import SparkSession


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


def process_args(args):
    """
    Processa os argumentos passados para a função.\n
    Processes the arguments passed to the function.

    Args:
        args (list): Lista de argumentos.
                     List of arguments.

    Returns:
        dict: Dicionário de propriedades raiz.
              Dictionary of root properties.
    """
    root_properties = {}
    for i, arg in enumerate(args):
        if arg.startswith('-'):
            root_properties[arg.replace('-', '')] = args[i + 1]
    return root_properties


def main(args=sys.argv[1:]):

    # Processa os argumentos
    # Process the arguments
    root_properties = process_args(args)

    # Imprime as propriedades raiz
    # Print the root properties
    for p in root_properties:
        log_info(f'{p}: {root_properties[p]}')

    table_name = root_properties['table_name']

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


if __name__ == '__main__':
    main()
