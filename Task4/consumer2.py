#!/usr/bin/env python3
import sys
import json
from kafka import KafkaConsumer

#Like
topic = sys.argv[1]

consumer = KafkaConsumer(topic)

data = {}

def sortDict(d):
    sorted_list = sorted(d.items())
    t={}
    for key,value in sorted_list:
        t[key]=value
    return t

#Subscribed to Like
for message in consumer:
    message = message.value.decode()
    if message == 'EOF':
        break
    
    message = message.split(" ")

    if(message[1] not in data):
        data[message[1]]={}

    if(message[2] not in data[message[1]]):
        data[message[1]][message[2]] = 0

    data[message[1]][message[2]] += 1

data=sortDict(data)
print(json.dumps(data, indent=4))
