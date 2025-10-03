import pika
import json
from config import RABBITMQ_URL, EXCHANGE_NAME

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')

channel.queue_declare(queue='login_queue')
channel.queue_bind(exchange=EXCHANGE_NAME, queue='login_queue', routing_key='user.login')

def callback(ch, method, properties, body):
    mensagem = json.loads(body)
    print(f"[LOGIN] {mensagem['user']} acabou de fazer login!")

channel.basic_consume(queue='login_queue', on_message_callback=callback, auto_ack=True)

print("[LOGIN] Aguardando mensagens de login...")
channel.start_consuming()
