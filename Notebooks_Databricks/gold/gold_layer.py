# Databricks notebook source
# Importando bibliotecas PySpark 

from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import *
#from pyspark.sql import SparkSession

# COMMAND ----------

df_gold = spark.table('workspace.silver.crypto_exchange')

df_gold.limit(5).display()


# COMMAND ----------

df_gold = df_gold.withColumn('spread',col('ask_price')-col('bid_price'))\
    .withColumn('spread_pct', (col("ask_price")-col("bid_price"))/col("exchange_rate"))

df_gold.limit(5).display()

# COMMAND ----------

w_price_ystd = Window.partitionBy('crypto_code','converted_code').orderBy('last_refreshed_date')

df_gold = df_gold.withColumn('price_today', col('exchange_rate'))\
    .withColumn('price_yesterday', lag('exchange_rate').over(w_price_ystd))\
        .withColumn('perc_change', (col('price_today')-col('price_yesterday')) / col('price_yesterday'))

df_gold.limit(5).display()

# COMMAND ----------

w_priority = Window.partitionBy('crypto_code','converted_code').orderBy(desc('last_refreshed_date'))

df_gold = df_gold.withColumn('priority', row_number().over(w_priority))
df_gold.limit(5).display()

# COMMAND ----------

w_rank_price = Window.orderBy(desc(col('price_today')))

df_gold = df_gold.withColumn('price_rank', rank().over(w_rank_price))\
    .withColumn('best_spread_rank', rank().over(Window.orderBy('spread')))\
    .withColumn('best_spread_pct_rank', rank().over(Window.orderBy('spread_pct')))

df_gold.limit(5).display()


# COMMAND ----------

df_gold.printSchema()

# COMMAND ----------

df_gold.write.mode('overwrite').format('delta').saveAsTable('workspace.gold.crypto_metrics')

spark.sql("""
    SELECT * 
    FROM gold.crypto_metrics
    LIMIT 10 
""").display()

# COMMAND ----------

