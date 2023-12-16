#!/usr/bin/env python3
import sys


def cleanLine(line):
    line=line.strip()
    if line == '[':
        return ''
    
    if line == ']':
        return '' 
    
    if line[-1] == ',':
        return line[:-1]
    
    return line

def calculateStrikeRate(runs,balls):
    if balls==0:
        return round(0,3)
    return round((runs/balls)*100,3)



for line in sys.stdin:
    cleaned_line = cleanLine(line)
    if(cleaned_line==''):
        continue
    object =eval(cleaned_line) #convert line to dictionary
    
    result={'name':object['name'],'local_strike_rate':calculateStrikeRate(object['runs'],object['balls'])}

    print(result)

	
