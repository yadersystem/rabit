import pika
import time
import random



# Canal para convertirse en publisher o suscribers
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')


def callback(ch,method,properties,body):
    # calculo  tiempo de dormir 1 a 10S
    #randon= random.randrange(10)
    # print body + tiempo de dormir
    #print(f'[X]recived: {body.decode()}'+str(randon))
    #Duermo
    #time.sleep(randon)
    #print(f'[X]recived: {body.decode()}')
    print(method)
    sleeptime=int(random.randrange(1,11))
    print(f'{body.decode()}and sleep{sleeptime}')
    time.sleep(sleeptime)
    print(f'[X]recived: {body.decode()}')
    ch.basic_consume(queue='test',on_message_callback=callback)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test', on_message_callback=callback,auto_ack=True)

print('Waiting for a message...')
channel.start_consuming()