import paho.mqtt.client as mqtt
import pyaes
import hashlib

def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    client.subscribe("Test/#")

key = "4u7x!A%D*G-KaPdRgUkXp2s5v8y/B?E("
key = key.encode('utf-8')
aes = pyaes.AESModeOfOperationCTR(key)

def on_message( client, userdata, msg):
    pesan1 = "Decrypted : "
    msg = msg.payload
    print(msg)
    decrypted = aes.decrypt(msg).decode('utf-8')
    #print(pesan1+decrypted)

    n = 128
    parts = [decrypted[i:i + n] for i in range(0, len(decrypted), n)]
    hashValue = ''.join(parts[0])
    pesanAsli = ''.join(parts[1])
    #print("Hash Value : ",hashValue)
    print("Pesan : ",pesanAsli)

    m = hashlib.sha512()
    m.update(pesanAsli.encode('utf-8'))
    digest = m.hexdigest()
    #print("digest : ",digest)

    print(hashValue==digest)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set("mwmauqfp", "gHrpJvNsX447")
client.connect("m12.cloudmqtt.com", 13219, 60)
# client.username_pw_set("husnul", "husnul")
# client.connect("localhost", 1883, 60)

client.loop_forever()