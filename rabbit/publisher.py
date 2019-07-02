import pika

# Canal para convertirse en publisher o suscribers
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')

#body = input('Please type dont message:')
for x in range(1,11):
    print(f'[X]sent message{x}')
    #channel.basic_publish(exchange='', routing_key='test', body=body)
    channel.basic_publish(exchange='', routing_key='test', body=str(x))

print('[x] Sent')
connection.close()
