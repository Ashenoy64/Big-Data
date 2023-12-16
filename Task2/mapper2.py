#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line=line.strip()
    data = line.split('\t')

    if(int(data[-1])>=3 or int(data[-1])==-1):
        continue

    print(line)