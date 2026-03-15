# PROJECT_CONTEXT --- Real-Time Banking Data Pipeline

## Goal

Build a **real-time data engineering pipeline** that simulates banking
transactions, processes them with streaming technologies, and generates
analytics datasets for dashboards.

## Architecture

Transaction Generator → Kafka Producer → Kafka Topic → Spark Structured
Streaming → Data Lake (Parquet) → Spark SQL Analytics → CSV Export →
Tableau Dashboard

## Core Components

### Ingestion

-   Kafka + Zookeeper (Docker)
-   Python transaction producer

### Streaming Processing

-   Spark Structured Streaming
-   Transaction parsing and transformation

### Fraud Detection

-   Rule-based detection of high-value transactions

### Storage

-   Parquet-based Data Lake

### Analytics

-   Spark SQL analytics queries

### Visualization

-   CSV datasets for Tableau dashboards

## Technologies

-   Apache Kafka
-   Apache Spark (PySpark)
-   Docker
-   Python
-   Parquet Data Lake
-   Tableau

## Key Scripts

setup.sh\
Installs Java, Docker, Spark, and Python dependencies.

start_pipeline.sh\
Starts Kafka, producer, and streaming pipelines.

stop_pipeline.sh\
Stops Kafka and pipeline services.

## Pipeline Summary

Producer → Kafka → Spark Streaming → Parquet Data Lake → Spark SQL →
Dashboard CSV → Tableau

## Purpose

Demonstrate **modern streaming data architecture used in real-world data
engineering systems**.
