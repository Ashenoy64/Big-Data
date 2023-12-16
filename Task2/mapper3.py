#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line =line.strip()
    data = line.split('\t')
    print(f'{data[0]}\t{data[-2]}')