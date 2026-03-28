# Importando bibliotecas PySpark 

from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import *
from src.utils.logger import get_logger

logger = get_logger('bronze')
logger.info('Leitura dos arquivos brutos iniciada...')

try: 
    df = spark.read.option("multiline","true")\
        .json("/Volumes/workspace/default/lago_do_mago/raw_data/*.json")

    df = df.select("`Realtime Currency Exchange Rate`.*")

    df = df.withColumnRenamed('1. From_Currency Code','crypto_code').withColumnRenamed('2. From_Currency Name','crypto_name')\
    .withColumnRenamed('3. To_Currency Code','converted_code').withColumnRenamed('4. To_Currency Name','converted_name')\
    .withColumnRenamed('5. Exchange Rate','exchange_rate').withColumnRenamed('6. Last Refreshed','last_refreshed_date')\
    .withColumnRenamed('7. Time Zone','time_zone').withColumnRenamed('8. Bid Price','bid_price').withColumnRenamed('9. Ask Price','ask_price')\
    .withColumn('upload_date',current_timestamp())
    #.filter(col('crypto_code').isNotNull())

except Exception as e:
    logger.exception(f'Falha inesperada: {e}')
    raise

df.write.format('delta')\
    .mode('overwrite')\
    .saveAsTable('bronze.crypto_exchange')

logger.info('Tabela bronze.crypto_exchange atualizada com sucesso!!')

