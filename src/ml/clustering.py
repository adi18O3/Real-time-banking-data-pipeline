from pyspark.ml.clustering import KMeans
from src.utils.spark_session import create_spark_session

def run_clustering():
    spark, config = create_spark_session()
    df = spark.table("bank_customers_processed")

    kmeans = KMeans(featuresCol="scaledFeatures", k=4)
    model = kmeans.fit(df)

    clustered = model.transform(df)

    clustered.write.mode("overwrite").saveAsTable("bank_customer_clusters")

    model.save(f"s3a://{config['aws']['bucket']}/{config['models']['kmeans_path']}")

if __name__ == "__main__":
    run_clustering()