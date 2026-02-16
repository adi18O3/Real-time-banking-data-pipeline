from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, StandardScaler
from src.utils.spark_session import create_spark_session
from src.utils.logger import get_logger

logger = get_logger(__name__)

def run_preprocessing():
    spark, config = create_spark_session()

    bucket = config["aws"]["bucket"]
    raw_path = f"s3a://{bucket}/{config['paths']['raw_data']}"

    df = spark.read.csv(raw_path, header=True, inferSchema=True)

    indexer = StringIndexer(inputCol="Gender", outputCol="GenderIndex")
    assembler = VectorAssembler(
        inputCols=["Age", "Annual Income (k$)", "Spending Score (1-100)", "GenderIndex"],
        outputCol="features"
    )
    scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")

    pipeline = Pipeline(stages=[indexer, assembler, scaler])
    model = pipeline.fit(df)
    processed_df = model.transform(df)

    processed_df.write.mode("overwrite").saveAsTable("bank_customers_processed")

    logger.info("Preprocessing complete")

if __name__ == "__main__":
    run_preprocessing()