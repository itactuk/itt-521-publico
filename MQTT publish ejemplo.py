import time

import paho.mqtt.client as mqtt

broker_address = '192.168.77.23'

def publicar():
    # Client(client_id=””, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
    nombre_cliente = 'sensor_luz'
    client =mqtt.Client(nombre_cliente)

    #connect(host, port=1883, keepalive=60, bind_address="")
    client.connect(broker_address)

    # publish(topic, payload=None, qos=0, retain=False)
    client.publish("house/bulbs/bulb1","ON")

publicar()

while True:
    pass
