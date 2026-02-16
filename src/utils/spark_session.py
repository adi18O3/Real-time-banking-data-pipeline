from pyspark.sql import SparkSession
import yaml

def create_spark_session(config_path="configs/config.yaml"):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    spark = SparkSession.builder         .appName(config["spark"]["app_name"])         .enableHiveSupport()         .getOrCreate()

    return spark, config