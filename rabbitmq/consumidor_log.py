import pika
import json
from config import RABBITMQ_URL, EXCHANGE_NAME

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')
channel.queue_declare(queue='log_queue')

for routing_key in ['user.login', 'user.upload', 'user.logout']:
    channel.queue_bind(exchange=EXCHANGE_NAME, queue='log_queue', routing_key=routing_key)

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"[LOG] {mensagem['user']} executou o evento: {mensagem['event']}")

channel.basic_consume(queue='log_queue', on_message_callback=callback, auto_ack=True)

print("[LOG] Aguardando todos os eventos...")
channel.start_consuming()
