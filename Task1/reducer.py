#!/usr/bin/env python3
import sys
import json
Objects={}

def calculateAverageStrikeRate(strikeRates):
    return round(sum(strikeRates)/len(strikeRates),3)

for i in sys.stdin:
    line=i.strip()
    
    object=eval(line)
    if(object['name'] not in Objects):
        Objects[object['name']]=[object['local_strike_rate']]

    else:
        Objects[object['name']].append(object['local_strike_rate'])
         
for name in Objects:
    result={"name":name,"strike_rate":calculateAverageStrikeRate(Objects[name])}
    print(json.dumps(result))