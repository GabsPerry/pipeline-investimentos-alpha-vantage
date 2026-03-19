# Importando bibliotecas 
from pyspark.sql import functions as F

def silver_checks(df):
    if df.filter(F.col('exchange_rate') < 0).count() > 0:
        raise Exception('Data Quality Error: Silver Exchange Rate Negativo')
    if df.filter(F.col('crypto_code').isNull()).count() > 0:
        raise Exception('Data Quality Error: Silver Crypto Code Nulo')
    
    return True
