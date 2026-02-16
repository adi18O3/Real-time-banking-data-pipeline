from pyspark.sql.functions import when
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from src.utils.spark_session import create_spark_session

def run_classification():
    spark, config = create_spark_session()
    df = spark.table("bank_customers_processed")

    df = df.withColumn(
        "label",
        when(
            (df["Annual Income (k$)"] > 60) &
            (df["Spending Score (1-100)"] > 60),
            1
        ).otherwise(0)
    )

    train, test = df.randomSplit([0.8, 0.2])

    rf = RandomForestClassifier(
        featuresCol="scaledFeatures",
        labelCol="label"
    )

    model = rf.fit(train)
    predictions = model.transform(test)

    evaluator = BinaryClassificationEvaluator()
    print("AUC:", evaluator.evaluate(predictions))

    predictions.write.mode("overwrite").saveAsTable("bank_customer_predictions")

    model.save(f"s3a://{config['aws']['bucket']}/{config['models']['rf_path']}")

if __name__ == "__main__":
    run_classification()