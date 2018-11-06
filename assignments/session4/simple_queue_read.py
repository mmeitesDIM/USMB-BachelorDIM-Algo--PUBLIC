# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:23:33 2018

@author: meitesm
"""

# create a reader
import pika
import os
import amqpkey

ampq_url = amqpkey.key

url = os.environ.get('CLONDAMQP_URL',ampq_url )
params = pika.URLParameters(url)
params.socket_timeout = 15
#initiate connexion
connection = pika.BlockingConnection(params)

# initate a channel
channel = connection.channel()
channel.queue_declare(queue='Presentation')

def callback(ch,method,properties,body):
    print("[x] received %r" % body)

channel.basic_consume(callback,
                      queue='Presentation',
                      no_ack=True)

print('fin lecture')
channel.start_consuming()