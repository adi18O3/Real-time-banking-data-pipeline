# Running the Real-Time Banking Pipeline

This document explains how to run the project step by step.

The entire pipeline can be started using provided scripts.

---

# Step 1 — Clone the Repository

```bash
git clone <repository-url>
cd banking-bigdata-platform
```

---

# Step 2 — Install Dependencies

Run the setup script:

```bash
./scripts/setup.sh
```

This installs:

- Java 17
- Python dependencies
- Docker
- Spark

---

# Step 3 — Start the Data Pipeline

Run:

```bash
./scripts/start_pipeline.sh
```

This script will start:

- Kafka cluster
- Transaction producer
- Spark streaming pipeline
- Fraud detection pipeline

---

# Step 4 — Monitor Logs

You can monitor the running pipeline using logs.

**Producer logs**

```bash
tail -f producer.log
```

**Streaming pipeline logs**

```bash
tail -f streaming.log
```

**Fraud detection logs**

```bash
tail -f fraud.log
```

---

# Step 5 — Verify Data Lake

After a few seconds, data should be written to the data lake.

Check:

```bash
ls data_lake/transactions
```

You should see Parquet files.

---

# Step 6 — Run Analytics

Run analytics queries using Spark:

```bash
spark-submit warehouse/run_analytics.py
```

---

# Step 7 — Generate Dashboard Data

Create dashboard datasets:

```bash
spark-submit warehouse/export_for_dashboard.py
```

This will generate CSV files inside:

```
dashboard_data/
```

Files generated:

- `city_transactions.csv`
- `type_amounts.csv`
- `fraud_alerts.csv`

---

# Step 8 — Build Tableau Dashboard

Open Tableau and load the CSV files from:

```
dashboard_data/
```

Create visualizations such as:

- Transactions by city
- Transaction amount by type
- Fraud alerts

---

# Step 9 — Stop the Pipeline

To stop all services run:

```bash
./scripts/stop_pipeline.sh
```

---

# Troubleshooting

If Kafka containers are not running:

```bash
docker ps
```

Restart the pipeline:

```bash
docker compose down
./scripts/start_pipeline.sh
```

---

# Pipeline Summary

- Producer generates transactions
- Kafka ingests streaming data
- Spark processes transactions
- Fraud detection identifies suspicious transactions
- Data is stored in Parquet format
- Analytics datasets are created
- Tableau dashboards visualize the data

---
