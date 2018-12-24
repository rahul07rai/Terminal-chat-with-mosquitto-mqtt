import paho.mqtt.client as mqtt
import time
from client import Login
from db import add_text, get_text
from datetime import datetime

l = Login()
(pubtop, subtop) = l.userSelect()

def on_connect(client, userdata, flags, rc):
    print("Connected! rc:", rc)

def on_message(client, userdata, message):
    if str(message.topic) != pubtop:
        print(str(message.topic), ":",str(message.payload.decode("utf-8")))
        add_text(str(message.topic), pubtop, str(message.payload.decode("utf-8")), datetime.now())

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed:", str(mid), str(granted_qos))

def on_unsubscribe(client, userdata, mid):
    print("Unsubscribed:", str(mid))

def on_publish(client, userdata, mid):
    print("Publish:", client)

def on_log(client, userdata, level, buf):
    print("log:", buf)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


broker_address = "0.0.0.0"
port = 9001
client = mqtt.Client(transport='websockets')
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_connect = on_connect
client.on_message = on_message
time.sleep(1)

client.connect(broker_address, port)
client.loop_start()
client.subscribe(subtop)

while True:
    chat = input()
    if chat == 'QUIT':
        break
    elif chat == 'SUBSCRIBE':
        new_subtop = input('Subscribe to topic: ')
        client.subscribe(new_subtop)
    elif chat == 'UNSUBSCRIBE':
        unsubtop = input('Unsubscribe from topic: ')
        client.unsubscribe(unsubtop)
    elif chat == 'PUBLISH':
        pubtop = input('Publish to new topic: ')
    else:
        client.publish(pubtop, chat)

client.disconnect()
client.loop_stop()


