#!/usr/bin/env python3
import sys

hashMap2d ={}


for i in sys.stdin:
    line=i.strip()
    data = line.split('\t')
    
    if(data[0] not in hashMap2d):
        hashMap2d[data[0]]=dict()

    if(data[1] not in hashMap2d[data[0]]):
        hashMap2d[data[0]][data[1]] = [-1,-1]



    if(data[-1]=='order'):
        hashMap2d[data[0]][data[1]][0] = data[2]

    else:
        hashMap2d[data[0]][data[1]][1] = data[2]
    

for pid in hashMap2d:
    for data in hashMap2d[pid]:
        print(f'{pid}\t{data}\t{hashMap2d[pid][data][0]}\t{hashMap2d[pid][data][1]}')
         
