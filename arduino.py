
# Target: To instruct arduino
# Input: AWS 
# Output: Arduino

# pip install pyserial
# create a subscriber (receiver)

import paho.mqtt.client as mqtt
import serial

client=mqtt.Client()
client.connect('34.244.89.66',1883)
print('Broker Connected')

client.subscribe('VSSUT/bulb') # subscriber

# serial - class 
# create an object
ser = serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

# create a function def to send data to arduino
def send_to_arduino(k):
	ser.write(k) # ser.write() data will be written to arduino
	print('Data Sent to Arduino')

#send_to_arduino("on") # on will be sent to arduino
#send_to_arduino("off") # off will be sent to arduino

# define a function called notification
def notification(client,userdata,msg):
	t=(msg.payload) # msg - object, payload - key
	print(t)
	send_to_arduino(t) # on - bulb on, off - bulb off

# configure this notification
client.on_message=notification
client.loop_forever()

