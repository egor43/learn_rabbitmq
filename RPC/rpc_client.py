import pika
import uuid
import random

class FibonacciRpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        method_frame = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue_name = method_frame.method.queue
        self.channel.basic_consume(queue=self.callback_queue_name,
                                   on_message_callback=self.on_response,
                                   auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue_name,
                                                                   correlation_id=self.correlation_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

for _ in range(random.randint(5, 15)):
    n = random.randint(5, 20)
    print(f'Requesting: fib({n})')
    response = fibonacci_rpc.call(n)
    print(f'Response: {response}')     
