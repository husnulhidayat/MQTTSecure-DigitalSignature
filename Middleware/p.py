import sys
import getopt
import paho.mqtt.client as mqtt
import pyaes
import configparser
import hashlib
import time
import psutil
import base64

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


def on_connect( client, userdata, flags, rc):
    print ("Connected with Code : " +str(rc))
    #client.subscribe(topic)

def on_message( client, userdata, msg):
    print(str(msg.payload))

def on_log(client, userdata, level, buf):
    print("log: ",buf)


client = mqtt.Client()
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

def main(argv):
    try:
        opts, args, = getopt.getopt(argv,"h:m:d:",["message=","log="])
    except getopt.GetoptError:
        print("python3 {p.py} -m {message} -d {}")
        print("log:")
        print("enable = 1")
        sys.exit(0)
    for opt, arg in opts:
        if opt == "h":
            print("python3 {p.py} -m {message} -d {}")
            print("log:")
            sys.exit(0)
        elif opt in ("-m","--message"):
            message = arg
        elif opt in ("-d","--log"):
            log = arg
            if (log=="1"):
                client.on_log = on_log
            else:
                print("invalid syntax: ")
                sys.exit(0)

    #print(message.encode('utf-8'))
    hash = hashlib.sha512()
    hash.update(message.encode('utf-8'))
    digest = hash.hexdigest()
    #print(digest)

    # joinvalue#
    join = digest + message
    #print(join)

    # createdigitalsignature
    digitalsignature = aes.encrypt(join)

    # show send time to broker
    # showing ds value
    #print("digital signature ", digitalsignature.hex())
    # end
    client.publish(topic, digitalsignature, qos=qosval)
    print('published successfully')


if __name__ == '__main__':
    main(sys.argv[1:])
