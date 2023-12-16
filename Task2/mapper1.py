#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    data = line.split('\t')
    if data[0]=='order':
        print(f'{data[3]}\t{data[2]}\t{data[4]}\torder')
    else:
        print(f'{data[2]}\t{data[3]}\t{data[4]}\treview')

	
