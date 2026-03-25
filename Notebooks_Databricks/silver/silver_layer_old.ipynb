# Databricks notebook source
# Importando bibliotecas PySpark 

from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import *
#from pyspark.sql import SparkSession

# COMMAND ----------

df_silver = spark.sql("""
    SELECT * 
    FROM bronze.crypto_exchange
""")
df_silver = df_silver.withColumn('last_refreshed_date', substring(col('last_refreshed_date'),1,10).cast(DateType()))

df_silver.printSchema()

# COMMAND ----------

df_silver = df_silver.withColumn('exchange_rate', col('exchange_rate').cast(DoubleType())).withColumn('bid_price', col('bid_price').cast(DoubleType()))\
.withColumn('ask_price', col('ask_price').cast(DoubleType()))

df_silver.printSchema()

# COMMAND ----------

df_silver.limit(5).display()

# COMMAND ----------

# Dedup da silver (estou mantendo arquivos e linhas repetidas na bronze)
dedup = Window.partitionBy('crypto_code','converted_code','last_refreshed_date').orderBy(desc('upload_date'))

df_silver = df_silver.withColumn('dp', row_number().over(dedup))\
    .filter('dp = 1')\
    .drop('dp')

df_silver.show(5)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ALTER TABLE silver.crypto_exchange 
# MAGIC -- SET TBLPROPERTIES (
# MAGIC --   'delta.feature.allowColumnDefaults' = 'supported'
# MAGIC -- );
# MAGIC
# MAGIC -- ALTER TABLE silver.crypto_exchange 
# MAGIC -- ALTER COLUMN updated_date SET DEFAULT current_timestamp() 
# MAGIC
# MAGIC -- ALTER TABLE silver.crypto_exchange 
# MAGIC -- ALTER COLUMN updated_date DROP DEFAULT;
# MAGIC
# MAGIC DESCRIBE DETAIL silver.crypto_exchange;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE EXTENDED silver.crypto_exchange;

# COMMAND ----------

df_silver.limit(5).display()

# COMMAND ----------

# df_silver.withColumn('updated_date', current_timestamp())\
# .write.format('delta')\
#     .mode('overwrite')\
#     .saveAsTable('silver.crypto_exchange')

querySQL = spark.sql("""
    SELECT * 
    FROM silver.crypto_exchange
    LIMIT 10
""") 

querySQL.display()

# COMMAND ----------

df_silver.createOrReplaceTempView("temp_vw_df_silver")

merge = spark.sql("""
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

merge.show()

querySQL = spark.sql("""
    SELECT * 
    FROM silver.crypto_exchange
    LIMIT 10
""") 

querySQL.show()

# COMMAND ----------

