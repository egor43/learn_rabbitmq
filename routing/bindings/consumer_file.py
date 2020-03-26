import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Создаем очередь для данного подключения
method_frame = channel.queue_declare(queue='', exclusive=True)
queue_name = method_frame.method.queue


# Привязываем очередь с типом ERROR к обменнику "direct_logs"
channel.queue_bind(exchange='direct_logs', queue=method_frame.method.queue, routing_key='ERROR')

def callback(ch, method, properties, body):
    with open('error_log.log', 'a') as file:
        file.write(f'[{method.routing_key}] {body.decode()}\n')

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
