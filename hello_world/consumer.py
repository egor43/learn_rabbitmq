import pika

print('Consumer connecting...')
# Подключение
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print('Connected.')

# Создаем очередь. Создание очереди - идемпотентно, т.е. можно запускать сколько угодно раз, но очередь будет только одна.
channel.queue_declare(queue='hello')

# Создаем коллбек на сообщение
def callback(ch, method, properties, body):
    print(f'Callback: ch: {ch}; method: {method}; properties: {properties}')
    print(f'---> Message: {body}')

# Регистрируем колбек
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print('Waiting message...')
# Ожидаем новых сообщений
channel.start_consuming()
