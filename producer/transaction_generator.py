import random
import time
from faker import Faker

fake = Faker()

transaction_types = ["Credit", "Debit", "Transfer", "Refund", "Payment"]

locations = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane",
    "Bhopal", "Visakhapatnam", "Patna", "Vadodara", "Agra"
]

def generate_transaction():

    transaction = {
        "transaction_id": fake.uuid4(),
        "customer_id": fake.random_int(1000, 9999),
        "transaction_type": random.choice(transaction_types),
        "amount": round(random.uniform(100, 10000), 2),
        "location": random.choice(locations),
        "timestamp": int(time.time())
    }

    return transaction
