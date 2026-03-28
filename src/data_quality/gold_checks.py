from pyspark.sql import functions as F

def gold_validation(df):
    
    if df.count() == 0:
        raise Exception('Data Quality Error: Gold truncada')

    required_cols = [
        'exchange_rate',
        'spread',
        'spread_pct',
        'price_today',
        'priority',
        'price_rank',
        'best_spread_rank',
        'best_spread_pct_rank'
    ]
    
    #if df.filter(F.col('perc_change').isNull()).count() > 0:
    #    raise Exception('Data Quality Error: Gold Percentual Change Nulo')
    
    if df.filter(F.col('spread') < 0).count() > 0:
        raise Exception('Data Quality Error: Gold Spread Negativo')

    for col in required_cols:
        if df.filter(F.col(col).isNull()).count() > 0:
            raise Exception(f'Data Quality Error: Gold métrica {col} nula')
    
    return True
