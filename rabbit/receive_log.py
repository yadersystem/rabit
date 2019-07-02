import sys

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

#para consumidor una cola
result_queue = channel.queue_declare(queue='',exclusive=True)

queue_name=result_queue.method.queue

list =sys.argv[1:]

for x in list:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=x)


def callback(ch,method,properties, body):
    #print(f'[X] recived {body.decode()}')
    print(eval(body)['type'])
    #type = eval(body)["type"]
    #message = eval(body)["message"]


channel.basic_consume(queue=queue_name, on_message_callback=callback,auto_ack=True)

print('Starting Consuming ...')
channel.start_consuming()