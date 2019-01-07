# MQTTSecure-DigitalSignature
is a middleware to secure the payload sent from the publisher to the subscriber, securing the middleware implements AES and SHA to create Digital Signature, the middleware is made with python 3.
# Development Software and Hardware
- Python 3.5.2
- Raspberry Pi
- NodeMCU
# External Library
- Paho-mqtt
- Pyaes
- Configparser
- Hashlib
# How to use
- Clone this project
```
git clone https://github.com/husnulhidayat/MQTTSecure-DigitalSignature/
```
- Open middleware folder and install library requirements
```
pip3 install -r requirements.txt
```
- To open publisher
```
python3 publish.py
```
- To open subscriber
```
python3 subscribe.py
```
- You can adjust the MQTT configuration in **config** folder

**cheer 😀**




