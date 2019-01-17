import sys
import getopt
import paho.mqtt.client as mqtt
import pyaes
import configparser
import hashlib
import time
import psutil
import base64
import argparse

config = configparser.RawConfigParser()
config.read('config/config-publisher.txt')
username = config.get('credential','username')
password = config.get('credential','password')
topic = config.get('credential','topic')
server = config.get('host','server')
port = config.getint('host','port')
keepalive = config.getint('host','keep-alive')
secretkey = config.get('key','key')
qosval = config.getint('credential','qos')
clientid = config.get('credential','client')


parser = argparse.ArgumentParser()
parser.add_argument("-m",help="message")
args = parser.parse_args()

def on_connect( client, userdata, flags, rc):
    print ("Connected with Code : " +str(rc))
    #client.subscribe(topic)

def on_message( client, userdata, msg):
    print(str(msg.payload))

def on_log(client, userdata, level, buf):
    print("log: ",buf)


client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.loop_start()
time.sleep(1)

key = secretkey
key = key.encode('utf-8')
counter = pyaes.Counter(initial_value=0)
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)

def main():
    client.loop_start()
    try:
        #get message from arg
        message = args.m

        #create hashlib & hash message
        hlib = hashlib.sha512()
        hlib.update(message.encode('utf-8'))
        hash = hlib.hexdigest()

        #join message+hash
        join = hash+message

        #encrypting
        cipher = aes.encrypt(join)

        #publishing cipher to broker
        client.publish(topic,cipher,qos=qosval)
        print('published succesfully')
        time.sleep(1)



    except KeyboardInterrupt:
        print('intrupted')
        sys.exit(0)

    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    main()