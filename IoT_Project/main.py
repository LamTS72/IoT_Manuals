import sys
from Adafruit_IO import MQTTClient
import time
import random

#list of IO_feed
AIO_FEED_ID = ["button1", "button2"]
#username_AIO
AIO_USERNAME = "sonlam7220"
#key_AIO
AIO_KEY = "aio_rFgm643abQ5afZ3fdgVTEExgNG6k"

def connected(client):
    print("Connected successful ...")
    for i in AIO_FEED_ID:
        client.subscribe(i)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe successful ...")

def disconnected(client):
    print("Disconnected...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_number = 0
while True:
    counter -= 1
    if counter <= 0:
        counter = 10
        print("Random data is publishing...")
        if sensor_number == 0:
            print("Temperature...")
            temp = random.randint(10, 50)
            client.publish("sensor1", temp)
            sensor_number += 1
        elif sensor_number == 2:
            print("Light...")
            light = random.randint(50, 500)
            client.publish("sensor2", light)
            sensor_number += 1
        else:
            print("Moisture...")
            mois = random.randint(0, 100)
            client.publish("sensor3", mois)
            sensor_number = 0

    time.sleep(0.2)
    pass