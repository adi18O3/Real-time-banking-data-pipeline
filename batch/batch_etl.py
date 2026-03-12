from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BankBatchETL") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw/bank.csv",
    header=True,
    inferSchema=True
)

df_clean = df.dropna()

df_clean.write \
    .mode("overwrite") \
    .parquet("data/processed/bank_data")
