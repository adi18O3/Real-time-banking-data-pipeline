import random
import time
from faker import Faker

fake = Faker()

TRANSACTION_TYPES = [
    "withdrawal",
    "deposit",
    "transfer",
    "payment"
]

def generate_transaction():

    transaction = {
        "transaction_id": fake.uuid4(),
        "customer_id": fake.random_int(1000, 9999),
        "transaction_type": random.choice(TRANSACTION_TYPES),
        "amount": round(random.uniform(100, 10000), 2),
        "location": fake.city(),
        "timestamp": int(time.time())
    }

    return transaction
