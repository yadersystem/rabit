import sys
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

#message = "Hello world"
# Capturando los datos por terminal
message = " ".join(sys.argv[2:])
type= sys.argv[1].lower()

# Converitimos a diccionario
body = {'type':type , 'message':message}

# Pasamos el diccionario a json
bodyjson = json.dumps(body)

#print("Json: " + bodyjson)
channel.basic_publish(exchange='direct_logs',routing_key='',body=bodyjson)

#print('[X] sent')

connection.close()