

from kafka import KafkaProducer
import json
import time
import random

# Define Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Simulating user activity data
user_actions = ["login", "view", "purchase", "logout"]

def generate_user_activity():
    return {
        "user_id": random.randint(1, 1000),
        "action": random.choice(user_actions),
        "timestamp": int(time.time())
    }

# Stream data to Kafka
while True:
    activity = generate_user_activity()
    producer.send('user-activity', activity)  
    print(f"Produced: {activity}")
    time.sleep(1)  # Delay to simulate real-time streaming

