#!/usr/bin/env python3
import sys
import json
from kafka import KafkaConsumer

def sortDict(d):
    sorted_list = sorted(d.items())
    t={}
    for key,value in sorted_list:
        t[key]=value
    return t


#Like
topic = sys.argv[3]

consumer = KafkaConsumer(topic)

data = {}


#Subscribed to Comment
for message in consumer:
    message = message.value.decode()
    if message == 'EOF':
        break
    
    message = message.split(" ")
    if(message[1] not in data):
        data[message[1]]=[]
    
    print(message)
    data[message[1]].append(message[2])

data=sortDict(data)
print(json.dumps(data, indent=4))


