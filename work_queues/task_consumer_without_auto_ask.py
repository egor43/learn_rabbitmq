import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f'Recieve: {body}')
    time.sleep(body.count(b'.'))
    print(f'Done')
    # Отвечаем кролику, что сообщение обработано
    ch.basic_ask(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='hello', on_message_callback=callback)

print('Waiting message...')
# Ожидаем новых сообщений
channel.start_consuming()
