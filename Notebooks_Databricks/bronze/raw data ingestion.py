# Databricks notebook source
# Importando bibliotecas PySpark 

from pyspark.sql.functions import * 
from pyspark.sql.types import * 
from pyspark.sql.window import *
#from pyspark.sql import SparkSession

# COMMAND ----------

# Listando diretório que criei no catalog
display(dbutils.fs.ls("/Volumes/workspace/default/lago_do_mago/raw_data"))

# COMMAND ----------

# Meu arquivo json tem quebra de linha (multiline), ou seja, um objeto json identado em várias linhas ao invés da mesma lnha
# Então preciso especificar para o Spark conseguir ler os arquivos  
df = spark.read.option("multiline","true").json("/Volumes/workspace/default/lago_do_mago/raw_data/*.json")
df.printSchema()

# COMMAND ----------

df = df.select("`Realtime Currency Exchange Rate`.*")
df.limit(5).display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS gold;
# MAGIC
# MAGIC SHOW SCHEMAS;

# COMMAND ----------

df = df.withColumnRenamed('1. From_Currency Code','crypto_code').withColumnRenamed('2. From_Currency Name','crypto_name')\
.withColumnRenamed('3. To_Currency Code','converted_code').withColumnRenamed('4. To_Currency Name','converted_name')\
.withColumnRenamed('5. Exchange Rate','exchange_rate').withColumnRenamed('6. Last Refreshed','last_refreshed_date')\
.withColumnRenamed('7. Time Zone','time_zone').withColumnRenamed('8. Bid Price','bid_price').withColumnRenamed('9. Ask Price','ask_price')\
.withColumn('upload_date', current_timestamp()).filter(col('crypto_code').isNotNull())

df.limit(5).display()

# COMMAND ----------

# Criando quando não existe a tabela bronze, alimentando quando existir
df.write.format('delta')\
    .mode('append')\
    .saveAsTable('bronze.crypto_exchange')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM bronze.crypto_exchange
# MAGIC LIMIT 10

# COMMAND ----------

