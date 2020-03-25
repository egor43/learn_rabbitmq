# Справедливая отправка сообщений. При настройке channel.basic_qos(prefetch_count=1)
# RabbitMQ не отправляет сообщение consumer'y пока тот не обработает текущее сообщение.

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Насраиваем справедливую отправку сообщений
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='task_fair')

message = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='', routing_key='task_fair', body=message)
print(f'Sent: {message}')
