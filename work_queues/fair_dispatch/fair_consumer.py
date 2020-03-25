# Справедливое получение сообщений. При настройке channel.basic_qos(prefetch_count=1)
# RabbitMQ не отправляет сообщение consumer'y пока тот не обработает текущее сообщение.

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_fair')
# Настраиваем справедливое получение
channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print(f'Recieve: {body}')
    time.sleep(body.count(b'.'))
    # Отвечаем кролику, что сообщение сначала обработается и только потом нужно отправлять следующее
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f'Done')


channel.basic_consume(queue='task_fair', on_message_callback=callback)

print('Waiting message...')
# Ожидаем новых сообщений
channel.start_consuming()
