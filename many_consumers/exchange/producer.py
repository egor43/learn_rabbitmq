# Публикация в несколько очередей

import pika
import sys

# Создание соединения
print('Producer connecting...')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print('Connected.')

# Создание обменника с названием "logs" и типом "fanout" (все полученные сообщения во все очереди)
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = sys.argv[1]
# Публикация сообщения во все очереди с обменником 'logs'
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f'Sent: {message}')

# Закрываем соединение
print('Closing...')
connection.close()
print('Close.')
