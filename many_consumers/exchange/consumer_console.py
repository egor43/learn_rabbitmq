import pika

print('Consumer connecting...')
# Подключение
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
print('Connected.')

# Создаем очередь со случайным именем (queue=''). Дополнительно, если соединение закрыто - удалить очередь (exclusive=True)
method_frame = channel.queue_declare(queue='', exclusive=True) # Возвращает объект из которого можно добыть полученное имя очереди

# Получаем имя очереди
queue_name = method_frame.method.queue

# Связываем обменник и очередь
channel.queue_bind(queue=queue_name, exchange='logs')

# Создаем коллбек на сообщение
def callback(ch, method, properties, body):
    print(f'---> Message: {body}')

# Регистрируем колбек
channel.basic_consume(queue=queue_name , auto_ack=True, on_message_callback=callback)

# Ожидаем новых сообщений
channel.start_consuming()
