from src.ingestion.upload_to_s3 import upload_to_s3
from src.etl.preprocess import run_preprocessing
from src.ml.clustering import run_clustering
from src.ml.classification import run_classification

def run_pipeline():
    upload_to_s3()
    run_preprocessing()
    run_clustering()
    run_classification()

if __name__ == "__main__":
    run_pipeline()