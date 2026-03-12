from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("StreamToDataLake") \
    .getOrCreate()

schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("customer_id", IntegerType()),
    StructField("transaction_type", StringType()),
    StructField("amount", DoubleType()),
    StructField("location", StringType()),
    StructField("timestamp", LongType())
])

# Read Kafka stream
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank_transactions") \
    .load()

json_df = kafka_df.selectExpr("CAST(value AS STRING) as json")

transactions = json_df.select(
    from_json(col("json"), schema).alias("data")
).select("data.*")

# Write streaming data to Parquet data lake
query = transactions.writeStream \
    .format("parquet") \
    .option("path", "data_lake/transactions") \
    .option("checkpointLocation", "data_lake/checkpoints") \
    .outputMode("append") \
    .start()

query.awaitTermination()
