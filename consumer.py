import json
from random import choice
import pandas as pd
from kafka import KafkaConsumer

from util import STOCKS

#Configura o KafkaConsumer para se conectar ao servidor Kafka e consumir mensagens de um tópico aleatório de transações de ações.
CONSUMER = KafkaConsumer(f'transaction_{choice(STOCKS)}', bootstrap_servers='localhost:19092', group_id='stock_group', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))


# Consome mensagens do Kafka e imprime no console.
def consume_transaction():
    for message in CONSUMER:
        print(f"Consumed: {message}")

# Inicia o consumo de transações quando o script é executado.        
if __name__ == '__main__':
    consume_transaction()