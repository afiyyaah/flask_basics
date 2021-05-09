import pika , json
params = pika.URLParameters('amqps://lcfsibhz:72y-Dec9z5U7ScU23vjAYtcvCyhXV-T8@baboon.rmq.cloudamqp.com/lcfsibhz')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties = properties)
