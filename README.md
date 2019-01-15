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
- Open middleware folder and install python library requirements
```
pip3 install -r requirements.txt
```
- You can adjust the MQTT configuration in **config** folder 😀
```
[credential] : your mqtt server info
[host]       : your host info
[key]        : your AES key (Use 32 byte key length)
```
- Open your publisher
```
python3 publish.py
```
- Open your subscriber
```
python3 subscribe.py
```




