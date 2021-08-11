# import library
import paho.mqtt.client as mqtt
from pymongo import MongoClient

# create a client object
client=mqtt.Client()
dbclient=MongoClient('127.0.0.1',27017)

# select the database
db=dbclient['vssut']

# select the collection
c=db['dht11']

# connect with broker
client.connect('172.31.20.66',1883)
print('Broker Conneted')

# create a subscription
client.subscribe('vssut/dht11')

# create a notification service
def notification(client,userdata,msg):
  t=(msg.payload).decode('utf-8')
  t=t.split(',')
  hum=t[1]
  temp=t[2]
  #print(hum,temp)
  k={} # dict in python
  k['hum']=hum
  k['temp']=temp
  print(k)
  c.insert_one(k) # inserting one document to collection
  print ('Data Stored in the collection')

# configure this notification
client.on_message=notification

client.loop_forever()
