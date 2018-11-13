import paho.mqtt.client as mqtt
import pyaes
import hashlib
import configparser


config = configparser.RawConfigParser()
config.read('config/config-subscriber.txt')
username = config.get('credential','username')
password = config.get('credential','password')
topic = config.get('credential','topic')
server = config.get('host','server')
port = config.getint('host','port')
keepalive = config.getint('host','keep-alive')
secretkey = config.get('key','key')

def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    client.subscribe(topic)

key = secretkey
key = key.encode('utf-8')
aes = pyaes.AESModeOfOperationCTR(key)

def on_message( client, userdata, msg):
    msg = msg.payload
    #print(msg)
    decrypted = aes.decrypt(msg).decode('utf-8')
    #print(pesan1+decrypted)

    n = 128
    parts = [decrypted[i:i + n] for i in range(0, len(decrypted), n)]
    hashValue = ''.join(parts[0])
    pesanAsli = ''.join(parts[1])
    #print("Hash Value : ",hashValue)
    print("")

    m = hashlib.sha512()
    m.update(pesanAsli.encode('utf-8'))
    digest = m.hexdigest()
    #print("digest : ",digest)

    if hashValue==digest:
        print("Pesan : ", pesanAsli)
        client.subscribe(topic)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set(username, password)
client.connect(server, port, keepalive)
# client.username_pw_set("husnul", "husnul")
# client.connect("localhost", 1883, 60)

client.loop_forever()