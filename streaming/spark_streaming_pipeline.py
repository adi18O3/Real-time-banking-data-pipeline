from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("BankStreamingPipeline") \
    .getOrCreate()

schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("customer_id", IntegerType()),
    StructField("transaction_type", StringType()),
    StructField("amount", DoubleType()),
    StructField("location", StringType()),
    StructField("timestamp", LongType())
])

# Read from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","bank_transactions") \
    .load()

# Convert Kafka value to string
json_df = kafka_df.selectExpr("CAST(value AS STRING) as json")

# Parse JSON
transactions = json_df.select(
    from_json(col("json"), schema).alias("data")
).select("data.*")

# Aggregation
aggregated = transactions.groupBy(
    "transaction_type"
).agg(
    sum("amount").alias("total_amount"),
    count("*").alias("txn_count")
)

# Output
query = aggregated.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
