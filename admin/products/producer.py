import json
import pika

params = pika.URLParameters(
    'amqps://ivzdrafs:ayWp8Y9LV_TUCuHc5c_g7zQXiDJITB0t@kebnekaise.lmq.cloudamqp.com/ivzdrafs')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    # properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body='hello')