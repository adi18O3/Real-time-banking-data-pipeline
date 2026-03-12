from kafka import KafkaProducer
import json
import time
from transaction_generator import generate_transaction

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "bank_transactions"

def start_stream():

    print("Starting transaction stream...")

    while True:

        txn = generate_transaction()

        producer.send(TOPIC, txn)

        print(txn)

        time.sleep(1)


if __name__ == "__main__":
    start_stream()
