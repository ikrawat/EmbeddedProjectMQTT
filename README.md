# LearnMQTT
Learning MQTT.

In this project I am trying to learn MQTT based communication.
After diving into the Protocol itself, I have given this initial try.

Some notes-
----------
I am disregarding QoS part.
I have used websockets protocol, instead of mqtt protocol. -> Wanted to use javascript.
I have also skipped the authentication part. I will enable that as soon as TLS and OpenSSL start making 
sense to me :)

My Setup
========
I have used two Virtual Machines running Ubuntu. Machine named "PUB-SUB"  and Machine named "Broker".
Used a NAT Network configuration, so that the publisher, subscriber and broker are in same network.
(At this point of time, I do not have much clue how to setup AWS - EC2 instance.)

Machine name "PUB-SUB":
-----------------------
In above setup, the publisher and the subscriber, both are running in same machine.
The publisher is a program running in python.
While the subscriber program is running in javascript with a smallest lamest HTML UI.

Machine name "Broker"
---------------------
Here the Mosquitto broker is running as a systemd service.
Mosquitto broker is configured to run with below config. This configs are configured in file-
/etc/mosquitto/mosquitto.conf

listener 12345
listener 1883
protocol websockets
allow_anonymous true
