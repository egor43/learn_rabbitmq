import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_fair')

messages = ('1 ...........',
            '2 ...............',
            '3 ..............',
            '4 .........',
            '5 ...................',
            '6 ............',
            '7 ....',
            '8 ...',
            '9 ..',
            '10 ..............',
            '11 ...........',
            '12 ......................', 
            '13 ..',
            '14 ..',
            '15 ..',
            '16 ..',
            '17 ........................')

for message in messages:
    channel.basic_publish(exchange='', routing_key='task_fair', body=message)
print(f'Sent done')
