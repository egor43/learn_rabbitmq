import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f'Recieve: {body}')
    time.sleep(body.count(b'.'))
    print(f'Done')

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('Waiting message...')
# Ожидаем новых сообщений
channel.start_consuming()
