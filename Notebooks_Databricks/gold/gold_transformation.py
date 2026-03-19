# Importando bibliotecas PySpark 
from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import *

df_gold = spark.table('silver.crypto_exchange')

df_gold = df_gold.withColumn('spread', col('ask_price')-col('bid_price'))\
    .withColumn('spread_pct', (col('ask_price')-col('bid_price'))/col('exchange_rate'))

w_price_ystd = Window.partitionBy('crypto_code','converted_code').orderBy('last_refreshed_date')

df_gold = df_gold.withColumn('price_today', col('exchange_rate'))\
    .withColumn('price_yesterday', lag('exchange_rate').over(w_price_ystd))\
    .withColumn('perc_change', (col('price_today')-col('price_yesterday'))/col('price_yesterday'))

w_priority = Window.partitionBy('crypto_code','converted_code').orderBy(desc('last_refreshed_date'))

df_gold = df_gold.withColumn('priority', row_number().over(w_priority))

w_rank_price = Window.orderBy(desc(col('price_today')))

df_gold = df_gold.withColumn('price_rank', rank().over(w_rank_price))\
    .withColumn('best_spread_rank', rank().over(Window.orderBy('spread')))\
    .withColumn('best_spread_pct_rank', rank().over(Window.orderBy('spread_pct')))

#df_gold.write.mode('overwrite').format('delta').saveAsTable('workspace.gold.crypto_metrics') 

df_gold.createOrReplaceTempView('temp_vw_df_gold')

#spark.sql = ("""
#    MERGE INTO gold.crypto_metrics as A
#    USING temp_vw_df_gold as B 
#        ON A.crypto_code = B.crypto_code 
#        AND A.converted_code = B.converted_code 
#        AND A.last_refreshed_date = B.last_refreshed_date 
#    UPDATE SET 
#        
#""")
 
print("Merge Gold executado com sucesso \n")

metrics = spark.sql("""
  DESCRIBE HISTORY gold.crypto_metrics
""").select("operationMetrics").first()[0]

print("Resultado do MERGE:") 
print(f"Linhas inseridas: {metrics.get('numTargetRowsInserted', 0)}") 
print(f"Linhas atualizadas: {metrics.get('numTargetRowsUpdated', 0)}") 

