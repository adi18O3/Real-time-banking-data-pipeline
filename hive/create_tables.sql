CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

CREATE TABLE bank_customers_processed AS
SELECT * FROM default.bank_customers_processed;

CREATE TABLE bank_customer_clusters AS
SELECT * FROM default.bank_customer_clusters;

CREATE TABLE bank_customer_predictions AS
SELECT * FROM default.bank_customer_predictions;