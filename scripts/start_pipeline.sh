#!/bin/bash

echo "======================================"
echo "Starting Banking Big Data Pipeline"
echo "======================================"

echo "Starting Kafka Cluster..."
docker compose up -d

sleep 10

echo "Starting Kafka Producer..."

python producer/transaction_producer.py > producer.log 2>&1 &

echo "Producer started (logs: producer.log)"

sleep 5

echo "Starting Spark Streaming Pipeline..."

spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
streaming/stream_to_datalake.py > streaming.log 2>&1 &

echo "Streaming pipeline started (logs: streaming.log)"

sleep 5

echo "Starting Fraud Detection..."

spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
streaming/fraud_detection_stream.py > fraud.log 2>&1 &

echo "Fraud detection started (logs: fraud.log)"

echo ""
echo "Pipeline Running Successfully!"
echo ""
echo "View logs with:"
echo "tail -f producer.log"
echo "tail -f streaming.log"
echo "tail -f fraud.log"
