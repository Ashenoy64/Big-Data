#!/usr/bin/env python3
import sys

count={}

for line in sys.stdin:
    line =line.strip()
    data=line.split('\t')

    if(data[0] not in count):
        count[data[0]]=0

    count[data[0]]+=int(data[1])


for i in count:
    print(f"{i}\t{count[i]}")