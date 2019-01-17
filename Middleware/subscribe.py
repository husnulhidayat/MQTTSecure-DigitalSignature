import paho.mqtt.client as mqtt
import pyaes
import hashlib
import configparser
import time

# import psutil

config = configparser.RawConfigParser()
config.read('config/config-subscriber.txt')
username = config.get('credential', 'username')
password = config.get('credential', 'password')
topic = config.get('credential', 'topic')
server = config.get('host', 'server')
port = config.getint('host', 'port')
keepalive = config.getint('host', 'keep-alive')
secretkey = config.get('key', 'key')
clientid = config.get('credential', 'client')
#server = "192.168.1.158"


def on_connect(client, userdata, flags, rc):
    print("Connected with Code :" + str(rc))
    client.subscribe(topic)


key = secretkey
key = key.encode('utf-8')
counter = pyaes.Counter(initial_value=0)
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)


def on_message(client, userdata, msg):
    client = mqtt.Client()
    # start = time.time()
    msg = msg.payload
    # print(msg)
    decrypted = aes.decrypt(msg).decode('utf-8')
    # print(pesan1+decrypted)

    n = 128
    parts = [decrypted[i:i + n] for i in range(0, len(decrypted), n)]
    hashValue = ''.join(parts[0])
    pesanAsli = ''.join(parts[1])
    # print("Hash Value : ",hashValue)
    print("")

    m = hashlib.sha512()
    m.update(pesanAsli.encode('utf-8'))
    digest = m.hexdigest()
    # print("digest : ",digest)

    if hashValue == digest:
        # print("Message : ", pesanAsli)
        mout.append(pesanAsli)

    end = time.time()

    # processing time
    # btos = end-start
    # f = open('ptob.txt').readline()
    # print("execute time publisher-broker-subscriber (for local testing) : ",btos+float(f))
    # cpu_process = psutil.Process()
    # print("cpu usage percent : ",cpu_process.cpu_percent())
    # print("memory usage : ",cpu_process.memory_info()[0] / float(2 ** 20)," MiB")

    # end


client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.on_connect = on_connect

client.on_message = on_message
mout = []
client.loop_start()
while True:
    if len(mout) > 0:
        counter = pyaes.Counter(initial_value=0)
        aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
        print(mout.pop())
client.loop_stop()