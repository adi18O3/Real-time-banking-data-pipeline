from pyspark.sql.functions import *

def create_customer_segments(df):

    df = df.withColumn(
        "balance_segment",
        when(col("balance") < 1000, "LOW")
        .when(col("balance") < 5000, "MEDIUM")
        .otherwise("HIGH")
    )

    return df
