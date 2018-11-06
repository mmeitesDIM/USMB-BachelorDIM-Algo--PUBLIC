# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:40:15 2018

@author: meitesm
"""

# create a publisher
import pika
import os
import amqpkey

ampq_url = amqpkey.key

url = os.environ.get('CLONDAMQP_URL',ampq_url )
params = pika.URLParameters(url)
params.socket_timeout = 15

#initiate connexion
connection = pika.BlockingConnection(params)    # connect to CloudAI

channel = connection.channel()
channel.queue_declare(queue='Presentation')
channel.basic_publish(exchange='',
                      routing_key='Presentation',
                      body='Hello word')

print('fin émission')
connection.close()
