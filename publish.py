import time
import paho.mqtt.client as mqtt
import pyaes
import base64
import hashlib

def on_connect( client, userdata, flags, rc):
    print ("Connected with Code : " +str(rc))
    client.subscribe("Test/#")

def on_message( client, userdata, msg):
    print(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.username_pw_set("husnul", "husnul")
# client.connect("localhost", 1883, 60)

client.username_pw_set("mwmauqfp", "gHrpJvNsX447")
client.connect("m12.cloudmqtt.com", 13219, 60)

client.loop_start()
time.sleep(1)

key = "4u7x!A%D*G-KaPdRgUkXp2s5v8y/B?E("
key = key.encode('utf-8')
aes = pyaes.AESModeOfOperationCTR(key)


while True:
    print("Mulai Publish Message ")
    pesan = input("message : ")

    #aesencrypt
    #enc = aes.encrypt(pesan)
    #end
    #encHEX = enc.hex()
    #print("enc hex : ", encHEX)

    #print(pesan)

    m = hashlib.sha512()
    m.update(pesan.encode('utf-8'))
    digest = m.hexdigest()
    #print("digest : ",digest)

    #joinvalue#
    join = digest+pesan
    #print("join    :",join)
    #join = enc+digest

    #inisebabnya
    #createdigitalsignature
    digitalsignature = aes.encrypt(join)
    print("digital signature ",digitalsignature.hex())
    #end

    client.publish("Test",digitalsignature)

    time.sleep(3)
    print("")

client.loop_stop()
client.disconnect()