import json
from random import choice
import pandas as pd
from kafka import KafkaConsumer

from util import STOCKS


CONSUMER = KafkaConsumer(f'transaction_{choice(STOCKS)}', bootstrap_servers='localhost:19092', group_id='stock_group', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

def consume_transaction():
    
    for message in CONSUMER:
        print(f"Consumed: {message}")
        
if __name__ == '__main__':
    consume_transaction()