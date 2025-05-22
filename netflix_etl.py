import os
from pyspark.sql import SparkSession

# Caminho para a chave JSON de autenticação
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hopeful-timing-460610-c6-394d9f1c4714.json"

# Criação da sessão Spark
spark = SparkSession.builder \
    .appName("Netflix ETL") \
    .config("spark.jars", "jars/spark-bigquery-latest_2.12.jar,jars/gcs-connector-hadoop3-latest.jar") \
    .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", os.environ["GOOGLE_APPLICATION_CREDENTIALS"]) \
    .getOrCreate()

# Leitura do CSV
df = spark.read.csv("netflix_titles_nov_2019.csv", header=True, inferSchema=True)

# Processamento
movies_df = df.select("title", "type", "release_year").filter(df["type"] == "Movie")
year_counts = movies_df.groupBy("release_year").count().orderBy("release_year")

# Escrita no BigQuery com projeto e bucket temporário especificados
year_counts.write \
    .format("bigquery") \
    .option("table", "hopeful-timing-460610-c6.netflix_etl.year_counts") \
    .option("project", "hopeful-timing-460610-c6") \
    .option("temporaryGcsBucket", "matheus-etl-temp-bucket") \
    .save()
