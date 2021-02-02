from kafka import KafkaConsumer
import json

#configuração do kafka
brokers = ['localhost:9092']
topico = 'postgres.public.produto'

consumer = KafkaConsumer(topico, group_id = 'group1', bootstrap_servers = brokers)

print(consumer.topics())

for messagem in consumer:
    texto = json.loads(messagem.value.decode('utf-8'))
    print(texto)
    
    
