import time
import paho.mqtt.client as mqtt
import pyaes
import configparser
import hashlib
import time
import psutil

config = configparser.RawConfigParser()
config.read('config/config-publisher.txt')
username = config.get('credential','username')
password = config.get('credential','password')
topic = config.get('credential','topic')
server = config.get('host','server')
port = config.getint('host','port')
keepalive = config.getint('host','keep-alive')
secretkey = config.get('key','key')


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
aes = pyaes.AESModeOfOperationCTR(key)

global ptob
while True:
    print("Start publishing your message")
    pesan = input("message : ")

    start = time.time()

    m = hashlib.sha512()
    m.update(pesan.encode('utf-8'))
    digest = m.hexdigest()
    #print("digest : ",digest)

    #joinvalue#
    join = digest+pesan
    #print("join    :",join)
    #join = enc+digest

    #createdigitalsignature
    digitalsignature = aes.encrypt(join)

    #show send time to broker
    #showing ds value
    #print("digital signature ",digitalsignature.hex())
    #end

    client.publish("Test",digitalsignature)
    client.on_log = on_log

    end = time.time()
    #processing time
    #u can give # if u dont want to see this processing
    ptob = end-start
    print("execute time (digital signature system) : ",ptob)

    f = open('ptob.txt','w')
    f.write(str(ptob))
    f.close()

    cpu_process = psutil.Process()
    print("cpu usage percent : ",cpu_process.cpu_percent())
    print("memory usage : ",cpu_process.memory_info()[0] / float(2 ** 20)," MiB")

    time.sleep(1)
    print("")
    #end

def on_log(client, userdata, level, buf):
    print("log: ",buf)
client.on_log=on_log

client.loop_stop()
client.disconnect()

