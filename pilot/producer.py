import time 
import json 
import random 
from datetime import datetime
from data_generator import generate_inventory
from kafka import KafkaProducer

def serializer(message):
    return json.dumps(message).encode('utf-8')

# TODO expose endpoint into config file 
# TODO expose topic name into config file
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    print('Producer has been started')
    while True:
        new_event = generate_inventory() 
        print(f'Produce new event @ {datetime.now()} : payload = {str(new_event)}')
        producer.send('messages', new_event)

        time_to_sleep = random.randint(1,7)
        time.sleep(time_to_sleep)