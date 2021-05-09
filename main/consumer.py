import pika, json
from main import User , db
params = pika.URLParameters('amqps://lcfsibhz:72y-Dec9z5U7ScU23vjAYtcvCyhXV-T8@baboon.rmq.cloudamqp.com/lcfsibhz')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue = 'main')

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'user_created':
        user = User(id=data['id'], first_name=data['first_name'], last_name=data['last_name'], email=data['email'], mobile=data['mobile'])
        db.session.add(user)
        db.session.commit()
        print('User Created')
    
    elif properties.content_type == 'user_updated':
        user = User.query.get(data['id'])
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.email=data['email']
        user.mobile=data['mobile']
        db.session.commit()
        print('User Updated')

    elif properties.content_type == 'user_deleted':
        user = User.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('User Deleted')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack= True)

print('Started Consuming')

channel.start_consuming()

channel.close()
