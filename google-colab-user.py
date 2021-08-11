import paho.mqtt.client as mqtt

# create a client object
client=mqtt.Client()

while True:
  print ('Enter on to make bulb on')
  print ('Enter off to make bulb off')
  k=input('Enter choice: on/off')
  if(k=="on"):
    client.connect("34.244.89.66",1883)
    print('Broker Connected')
    client.publish('VSSUT/bulb','on')
  elif(k=="off"):
    client.connect("34.244.89.66",1883)
    print('Broker Connected')
    client.publish('VSSUT/bulb','off')
