# Работа с сообщениями и маршрутизация по шаблонам
#
# "*" - может заменить одно слово
# "#" - может заменить ноль или более слов 

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Объявляем обменник "topic_log" с типом доставки по шаблонам ("topic")
channel.exchange_declare(exchange='topic_log', exchange_type='topic')

routing = sys.argv[1] # Напирмер: CORE.INFO или MODULE.ERROR
log_msg = sys.argv[2]

# Публикация сообщения в обменник "topic_log" с ключом маршрутизации routing
channel.basic_publish(exchange='topic_log', routing_key=routing, body=log_msg)

connection.close()
