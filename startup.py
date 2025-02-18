from kafka.admin import KafkaAdminClient, NewTopic

from util import STOCKS

admin_client = KafkaAdminClient(
    bootstrap_servers='localhost:19092', 
)

topic_list = []

for stock in STOCKS:
    topic_list.append(NewTopic(name=f'transaction_{stock}', num_partitions=1, replication_factor=1))
    
admin_client.create_topics(new_topics=topic_list, validate_only=False)