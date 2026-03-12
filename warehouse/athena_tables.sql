CREATE EXTERNAL TABLE bank_transactions (

transaction_id STRING,
customer_id INT,
transaction_type STRING,
amount DOUBLE,
location STRING,
timestamp BIGINT

)
STORED AS PARQUET
LOCATION 's3://bank-data-lake/streaming/';
