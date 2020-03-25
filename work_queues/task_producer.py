# Скрипт генерирует "задачи" различной сложности. 
# Сложность задачи зависит от количества точек в сообщении. Например: "..." - задача со сложностью 3 (time.sleep(3))

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f'Sent: {message}')
