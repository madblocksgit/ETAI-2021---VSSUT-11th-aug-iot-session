
# DHT11 -> Arduino -> Raspberry Pi -> AWS Cloud -> MONGODB Server 

# Publisher - Raspberry Pi
# Broker - AWS 34.244.89.66
# Subscriber - MONGODB Server 

import paho.mqtt.client as mqtt
import serial
import time

client=mqtt.Client() # create a client object

def send_to_aws(k):
	print('Sending Data to AWS')
	client.connect('34.244.89.66',1883)
	client.publish('vssut/dht11',k)

ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

while True:
	if(ser.inWaiting()>0):
		t=(ser.readline())
		print (t)
		send_to_aws(t)
