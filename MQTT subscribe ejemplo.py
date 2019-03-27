import time

import paho.mqtt.client as mqtt

broker_address = '192.168.77.23'

def suscribir():
    print("crea nueva instancia")
    client = mqtt.Client("P1") #crea nueva instancia
    client.on_message=on_message #attach function to callback
    print("connecting to broker")
    client.connect(broker_address) #connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","house/bulbs/bulb1")
    client.subscribe("house/bulbs/bulb1")
    # print("Publishing message to topic","house/bulbs/bulb1")
    # client.publish("house/bulbs/bulb1","OFF")
    # time.sleep(4) # wait
    # client.loop_stop() #stop the loop

def on_message(client, userdata, message):
    print("mensaje recibido " ,str(message.payload.decode("utf-8")))
    print("topic del mensaje=",message.topic)
    print("qos del mensaje=",message.qos)
    print("retain flag=",message.retain)

suscribir()

while True:
    pass
