import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters('amqps://lcfsibhz:72y-Dec9z5U7ScU23vjAYtcvCyhXV-T8@baboon.rmq.cloudamqp.com/lcfsibhz')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue = 'admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack= True)

print('Started Consuming')

channel.start_consuming()

channel.close()
