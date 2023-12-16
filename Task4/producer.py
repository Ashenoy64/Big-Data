import sys
from kafka import KafkaProducer

# index 0-> like
# index 1-> share
# index 2 -> comment

topics =  sys.argv[1:]
mapper = {'like': 0, 'share':1,'comment':2}



producer = KafkaProducer()

for line in sys.stdin:
    line = line.strip()
    if(line == 'EOF'):
        break
    topic, data = line.split(" ",maxsplit=1)
    if(topic in mapper):
        producer.send(topics[mapper[topic]],data.encode())
    producer.flush()


#Tell consumer job is done
for i in topics:
    producer.send(i,b'EOF')
    producer.flush()

