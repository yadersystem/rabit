import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='direct')
#para consumidor una cola
result_queue = channel.queue_declare(queue='',exclusive=True)
queue_name=result_queue.method.queue

severities = sys.argv[1:]

if not severities:
    print('Please set severities on execution, debug,info,warning or error')
    exit(1)


def callback(ch,method,properties, body):
    print(f'[X] recived [{method.routing_key}] {body.decode()}')


channel.basic_consume(queue=queue_name, on_message_callback=callback,auto_ack=True)
print("Waiting Message ....")

