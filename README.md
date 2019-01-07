# MQTTSecure-DigitalSignature
is a middleware to secure the payload sent from the publisher to the subscriber, securing the middleware implements AES and SHA to create Digital Signature, the middleware is made with python 3.
# Development Software and Hardware
- Python 3.5.2
- Raspberry Pi
- NodeMCU
# External Library
1. Paho-mqtt
2. Pyaes
3. Configparser
4. Hashlib
# How to use
1. Clone this project
```
git clone https://github.com/husnulhidayat/MQTTSecure-DigitalSignature/
```
2. Open middleware folder and install library requirements
```
pip3 install -r requirements.txt
```
3. To open publisher
```
python3 publsh.py
```
To open subscriber
```
python3 subscribe.py
```
4. You can adjust the MQTT configuration in **config** folder




