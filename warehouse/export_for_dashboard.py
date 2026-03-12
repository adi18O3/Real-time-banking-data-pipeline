from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ExportDashboardData") \
    .getOrCreate()

df = spark.read.parquet("data_lake/transactions")

# Transactions by city
city_df = df.groupBy("location").count()
city_df.toPandas().to_csv("dashboard_data/city_transactions.csv", index=False)

# Transaction type summary
type_df = df.groupBy("transaction_type").sum("amount")
type_df.toPandas().to_csv("dashboard_data/type_amounts.csv", index=False)

# Fraud candidates
fraud_df = df.filter("amount > 8000")
fraud_df.toPandas().to_csv("dashboard_data/fraud_alerts.csv", index=False)

print("Dashboard data exported.")
