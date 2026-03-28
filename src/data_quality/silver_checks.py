# Importando bibliotecas 
from pyspark.sql import functions as F 
from pyspark.sql.window import *
from pyspark.sql.types import *

def silver_checks(df):
    
    double_cols = ['exchange_rate','bid_price','ask_price']

    dedup = Window.partitionBy('crypto_code', 'converted_code','last_refreshed_date').orderBy(F.desc('upload_date'))

    if df.filter(F.col('exchange_rate') < 0).count() > 0:
        raise Exception('Data Quality Error: Silver Exchange Rate Negativo')
    
    if df.filter(F.col('crypto_code').isNull()).count() > 0:
        raise Exception('Data Quality Error: Silver Crypto Code Nulo')
    
    if df.withColumn('dp', F.row_number().over(dedup))\
        .filter('dp > 1').count() > 0:
        raise Exception('Data Quality Error: Silver duplicada')

    for coluna in double_cols:
        col_type = df.schema[coluna].dataType
        if not isinstance(col_type, DoubleType):
            raise Exception(f'Data Quality Error: Silver {coluna} não foi convertida para Double')
    
    return True
