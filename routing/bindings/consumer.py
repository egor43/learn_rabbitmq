import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Создаем очередь для данного подключения
method_frame = channel.queue_declare(queue='', exclusive=True)
queue_name = method_frame.method.queue


# Привязываем очередь с типами INFO, WARNING, ERROR к обменнику "direct_logs"
for route_key in ('INFO', 'WARNING', 'ERROR'):
    channel.queue_bind(exchange='direct_logs', queue=method_frame.method.queue, routing_key=route_key)

def callback(ch, method, properties, body):
    print(f'[{method.routing_key}] {body}')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
