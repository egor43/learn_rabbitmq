# Привязка очередей по ключам

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создаем обменник с прямым типом обмена - "direct"
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

log_lvl = sys.argv[1]
log_msg = sys.argv[2]

# Публикация сообщения в обменник "direct_logs" с ключом маршрутизации log_lvl
channel.basic_publish(exchange='direct_logs', routing_key=log_lvl, body=log_msg)

connection.close()
