import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='direct')

severity = sys.argv[1] if len (sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or ""

channel.basic_publish(exchange='logs',routing_key=severity,body=message)
print(f'[X] sent {severity}:{message}')
connection.close()