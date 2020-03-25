# Реализация "живучей" очереди, которая даже после рестарта сервера будет восстановлена

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Объявляем "стойкую" (защищенную от падений) очередь.
# Причем нельзя менять уже существующие очереди
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:])

# Необходимо пометить сообщения, как "постоянные". delivery_mode = 2
channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))
print(f'Sent: {message}')
