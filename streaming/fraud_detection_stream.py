from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("FraudDetectionStream") \
    .getOrCreate()

schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("customer_id", IntegerType()),
    StructField("transaction_type", StringType()),
    StructField("amount", DoubleType()),
    StructField("location", StringType()),
    StructField("timestamp", LongType())
])

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","bank_transactions") \
    .load()

json_df = kafka_df.selectExpr("CAST(value AS STRING) as json")

transactions = json_df.select(
    from_json(col("json"), schema).alias("data")
).select("data.*")

# Fraud Rule
fraud_transactions = transactions.filter(col("amount") > 8000)

query = fraud_transactions.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
