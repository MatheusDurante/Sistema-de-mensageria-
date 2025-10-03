import pika
import json
from datetime import datetime

url = 'amqps://rohreguf:wyXXG4qi2HZa_K8MpFrtRN_cSVtDz5R7@jaragua.lmq.cloudamqp.com/rohreguf'

from config import RABBITMQ_URL, EXCHANGE_NAME

connection = pika.BlockingConnection(pika.URLParameters(url))
channel = connection.channel()

channel.exchange_declare(exchange=url, exchange_type='direct')

eventos = [
    {"user": "João", "event": "user.login"},
    {"user": "João", "event": "user.upload"},
    {"user": "João", "event": "user.logout"},
    {"user": "Maria", "event": "user.login"},
]

for evento in eventos:
    evento['timestamp'] = datetime.utcnow().isoformat() + "Z"
    mensagem = json.dumps(evento)
    routing_key = evento['event']
    
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=routing_key,
        body=mensagem.encode()
    )
    print(f"[PRODUTOR] Enviado: {mensagem}")

connection.close()
