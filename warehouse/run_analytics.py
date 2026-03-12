from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BankAnalytics") \
    .getOrCreate()

# Load transactions from data lake
df = spark.read.parquet("data_lake/transactions")

df.createOrReplaceTempView("transactions")

print("\n=== Total Transactions ===")
spark.sql("""
SELECT COUNT(*) as total_transactions
FROM transactions
""").show()

print("\n=== Total Transaction Amount by Type ===")
spark.sql("""
SELECT transaction_type,
       SUM(amount) as total_amount
FROM transactions
GROUP BY transaction_type
ORDER BY total_amount DESC
""").show()

print("\n=== Top Cities by Transaction Volume ===")
spark.sql("""
SELECT location,
       COUNT(*) as txn_count
FROM transactions
GROUP BY location
ORDER BY txn_count DESC
LIMIT 10
""").show()

print("\n=== Average Transaction Amount ===")
spark.sql("""
SELECT AVG(amount) as avg_transaction
FROM transactions
""").show()
