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

There is two way to open this middleware :
1. Client side look like
2. System look like
what is this? just run, i just randomly giving that weird name lol.

**Client Side**
- Open your publisher
```
~$ python3 publish.py
```
- Open your subscriber
```
~$ python3 subscribe.py
```
**or**

**System look like** //i don't know
- Open middleware folder
- Go to /executable binary folder
- Open your command line
  - in order to open subscriber, you just type
  ```
  ~$ ./subscriber
  ```
  - in order to open publisher
  ```
  ~$ ./publisher -m {message}
  ```
- u can use this thing also for help
```
~$ ./publisher -h
```






