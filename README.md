# Real-Time Banking Data Pipeline (Kafka + Spark + Data Lake)

This project implements a **real-time banking analytics pipeline** using streaming technologies and big data tools.

The system simulates banking transactions, processes them in real time using Apache Spark, stores them in a data lake, and generates analytics data for dashboards.

This project demonstrates how modern **data engineering pipelines** are built using streaming architectures.

---

# Architecture Overview

```
Transaction Generator
        │
        ▼
Kafka Producer
        │
        ▼
Kafka Topic
        │
        ▼
Spark Structured Streaming
        │
        ├── Fraud Detection
        │
        └── Data Lake Storage (Parquet)
                │
                ▼
            Spark SQL Analytics
                │
                ▼
          Dashboard Data (CSV)
                │
                ▼
           Tableau Dashboard
```

---

# Tech Stack

**Streaming**
- Apache Kafka
- Zookeeper

**Processing**
- Apache Spark Structured Streaming
- PySpark

**Storage**
- Data Lake (Parquet)

**Analytics**
- Spark SQL
- Pandas

**Visualization**
- Tableau

**Infrastructure**
- Docker
- Docker Compose
- Linux / WSL

---

# Project Structure

```
banking-bigdata-platform
│
├── producer
│   └── transaction_producer.py
│
├── streaming
│   ├── stream_to_datalake.py
│   └── fraud_detection_stream.py
│
├── warehouse
│   ├── run_analytics.py
│   └── export_for_dashboard.py
│
├── scripts
│   ├── setup.sh
│   ├── start_pipeline.sh
│   └── stop_pipeline.sh
│
├── data_lake
├── dashboard_data
│
├── docker-compose.yml
├── requirements.txt
│
├── README.md
└── RUN_PROJECT.md
```

---

# Features

- Real-time transaction simulation
- Streaming ingestion using Kafka
- Spark Structured Streaming processing
- Fraud detection logic
- Data lake storage in Parquet format
- Batch analytics using Spark SQL
- Dashboard-ready CSV generation

---

# Example Use Case

A bank wants to monitor transactions in real time and detect potentially fraudulent activities.

This system simulates such a pipeline:

- Incoming transactions are streamed through Kafka
- Spark processes transactions in real time
- High value transactions are flagged
- Processed data is stored in a data lake
- Analytics datasets are generated for dashboards

---

# Example Analytics

- Total transaction volume
- Transactions by location
- Transactions by type (deposit, withdrawal, transfer)
- Fraud alerts (high-value transactions)

---

# How to Run

See the **RUN_PROJECT.md** file for step-by-step instructions.

---

# Learning Outcomes

This project demonstrates:

- Real-time streaming architecture
- Kafka producer-consumer model
- Spark Structured Streaming pipelines
- Building a data lake
- Creating analytics datasets
- Connecting data pipelines to dashboards

---

# Future Improvements

- Add Airflow for orchestration
- Store data in AWS S3
- Query data using Athena or Presto
- Build a real-time dashboard
- Add ML fraud detection model
- Add monitoring using Prometheus and Grafana

---

# Author

Aditya Sharma  
Data Engineering / Big Data Project
