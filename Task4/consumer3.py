#!/usr/bin/env python3
import sys
import json
from kafka import KafkaConsumer

#Like
topic = sys.argv[1:]

consumer = KafkaConsumer()
consumer.subscribe(topic)

data= {}

def sortDict(d):
    sorted_list = sorted(d.items())
    t={}
    for key,value in sorted_list:
        t[key]=value
    return t


def like(msg):
    if(msg[1] not in data):
        data[msg[1]]=[0,0,0]

    data[msg[1]][0]+=1
    pass

def share(msg):
    if(msg[1] not in data):
        data[msg[1]]=[0,0,0]

    data[msg[1]][1]+=len(msg)-3

def comment(msg):
    if(msg[1] not in data):
        data[msg[1]]=[0,0,0]

    data[msg[1]][2]+=1
    pass


#Subscribed to Share
for _message in consumer:
    message = _message.value.decode()
    if message == 'EOF':
        break
    message =  message.split(' ')
    if(_message.topic == topic[0]):
        like(message)
    elif(_message.topic == topic[1]):
        share(message)
    else:
        comment(message)


result = {}

for i in data:
    result[i]= (data[i][0] + 20*data[i][1] + 5*data[i][2])/1000

result = sortDict(result)

print(json.dumps(result, indent=4))