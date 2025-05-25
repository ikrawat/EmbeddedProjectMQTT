# This code publishes the data on a MQTT server.
# Paho library was used in python module. It has lot of examples and docs available.
# The proker IP for me was 10.0.2.4
# The port which was configured for listening was 12345.
#
# At this point of time I am avoiding authentication. Still going through TLS and OpenSSL
# Also standard ports to be used, I still have to verify.

import paho.mqtt.client as mqtt
import time

brokerIp = "10.0.2.4"
brokerPort = 12345

def onMessage(client, userdata, msg):
	print(f"message: {msg.payload.decode()} on topid {msg.topic}")

def onConnect():
	print(f"Connected!")

client = mqtt.Client(transport="websockets")
client.on_message = onMessage
client.on_connect = onConnect

# connect to broker
client.connect(brokerIp, brokerPort, 60)

for i in range(1, 100000000):
	client.publish("test/topic", "Hello Dear " + str(i))
	time.sleep(1)

cliend.disconnect()
