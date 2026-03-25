# Importando bibliotecas PySpark 
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import *
from src.utils.logger import get_logger
from src.data_quality.silver_checks import silver_checks

logger = get_logger('silver')
logger.info('Iniciando transformação da silver')

try:
    df_silver = spark.table('bronze.crypto_exchange')\
        .withColumn('last_refreshed_date', substring(col('last_refreshed_date'),1,10).cast(DateType()))\
        .withColumn('exchange_rate', col('exchange_rate').cast(DoubleType()))\
        .withColumn('bid_price', col('bid_price').cast(DoubleType()))\
        .withColumn('ask_price', col('ask_price').cast(DoubleType()))

    dedup = Window.partitionBy('crypto_code','converted_code','last_refreshed_date').orderBy(desc('upload_date'))

    df_silver = df_silver.withColumn('dp', row_number().over(dedup))\
        .filter('dp = 1')\
        .drop('dp')

    logger.info('Iniciando checagem Data Quality da silver...')
    
    df_silver.createOrReplaceTempView('temp_vw_df_silver')

    df_check = spark.table('temp_vw_df_silver')
    silver_checks(df_check)

    logger.info('Checagem OK!! Nenhum problema encontrado.')
    logger.info('Executando merge na silver.crypto_exchange...')

    spark.sql("""
    MERGE INTO silver.crypto_exchange A 
        USING temp_vw_df_silver B 
            ON A.crypto_code = B.crypto_code 
            AND A.converted_code = B.converted_code 
            AND A.last_refreshed_date = B.last_refreshed_date
        WHEN MATCHED THEN 
            UPDATE SET 
                A.crypto_name = B.crypto_name
                , A.converted_name = B.converted_name
                , A.exchange_rate = B.exchange_rate
                , A.time_zone = B.time_zone
                , A.bid_price = B.bid_price
                , A.ask_price = B.ask_price
                , A.updated_date = current_timestamp()
        WHEN NOT MATCHED THEN 
            INSERT 
                (crypto_code, crypto_name, converted_code, converted_name, exchange_rate, last_refreshed_date, time_zone, bid_price, ask_price, upload_date, updated_date)
            VALUES 
                (B.crypto_code, B.crypto_name, B.converted_code, B.converted_name, B.exchange_rate, B.last_refreshed_date, B.time_zone, B.bid_price, B.ask_price, B.upload_date, NULL)
    """)

    logger.info('Tabela silver atualizada com sucesso!!')

    metrics = spark.sql("""
        DESCRIBE HISTORY silver.crypto_exchange
    """).select("operationMetrics").first()[0]

    print("\nResultado do MERGE:") 
    print(f"Linhas inseridas: {metrics.get('numTargetRowsInserted', 0)}") 
    print(f"Linhas atualizadas: {metrics.get('numTargetRowsUpdated', 0)}") 
    #print(f"Linhas deletadas: {metrics.get('numTargetRowsDeleted', 0)}") 

except Exception as e:
    logger.exception(f'Erro ao transformar a tabela silver: {e}')
    raise

