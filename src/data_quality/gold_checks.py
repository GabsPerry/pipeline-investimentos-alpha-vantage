from pyspark.sql import functions as F

def gold_validation(df):
    #if df.filter(F.col('perc_change').isNull()).count() > 0:
    #    raise Exception('Data Quality Error: Gold Percentual Change Nulo')
    if df.filter(F.col('spread') < 0).count() > 0:
        raise Exception('Data Quality Error: Gold Spread Negativo')
    
    return True