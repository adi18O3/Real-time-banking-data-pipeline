import boto3
import yaml
from src.utils.logger import get_logger

logger = get_logger(__name__)

def upload_to_s3():
    with open("configs/config.yaml") as f:
        config = yaml.safe_load(f)

    s3 = boto3.client("s3")
    bucket = config["aws"]["bucket"]
    key = config["paths"]["raw_data"]

    s3.upload_file("data/bank_data.csv", bucket, key)
    logger.info("Upload successful")

if __name__ == "__main__":
    upload_to_s3()