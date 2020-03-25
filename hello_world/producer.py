import pika

# Создание соединения
print('Producer connecting...')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print('Connected.')

# Создание очереди
channel.queue_declare(queue='hello')

# Публикация сообщения
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print('Sent "Hello World!"')

# Закрываем соединение
print('Closing...')
connection.close()
print('Close.')
