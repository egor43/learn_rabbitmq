import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

method_frame = channel.queue_declare(queue='', exclusive=True)
queue_name = method_frame.method.queue

# Получаем ключи роута которые привязывать к обменнику
binding_keys = sys.argv[1:]

for binding_key in binding_keys:
    channel.queue_bind(queue_name, exchange='topic_log', routing_key=binding_key)

def callback(ch, method, properties, body):
    print(f'[{method.routing_key}] {body.decode()}')

channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

channel.start_consuming()
