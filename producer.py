from datetime import datetime
from random import choice, randint, uniform
from time import sleep
from kafka import KafkaProducer
import json

from kazoo.client import KazooClient

from util import STOCKS

# Configura o KafkaProducer para se conectar ao servidor Kafka.
# Configura o KazooClient para se conectar ao Zookeeper.

PRODUCER = KafkaProducer(bootstrap_servers='localhost:19092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

ZK = KazooClient(hosts='localhost:2181')
ZK.start()
 
# Cria nós no Zookeeper para cada ação na lista STOCKS com um valor inicial aleatório.
for stock in STOCKS:
    try:
        ZK.create(f'/stock/{stock}', value=str(uniform(1000, 9000)).encode(), makepath=True)
    except Exception as e:
        print(e)



# Gera transações de compra e venda de ações aleatoriamente.
# Atualiza o valor da ação no Zookeeper.
# Envia a transação para o Kafka.
def produce_transaction():
    trade_type = ['buy', 'sell']
    
    while True:
        stock = choice(STOCKS)
        price = float(ZK.get(f'/stock/{stock}')[0].decode())
        quantity = randint(1, 10)
        op_type = choice(trade_type)
        variation = (uniform(1, 10) * quantity)
        if op_type == 'buy':
            ZK.set(f'/stock/{stock}', str(variation).encode())
        else:
            ZK.set(f'/stock/{stock}', str(variation).encode())
        transaction = {
            'stock': stock,
            'price': price,
            'variation': variation,
            'quantity': quantity,
            'trade_type': op_type,
            'timestamp': datetime.now().isoformat()
        }
        PRODUCER.send(f'transaction_{stock}', value=transaction)
        print(f"Produced: {transaction}")
        sleep(uniform(0.1, 1))


# Inicia a produção de transações quando o script é executado.        
if __name__ == '__main__':
    produce_transaction()