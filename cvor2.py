import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "iot/cvor2/vlaga"
CLIENT_ID = "cvor2"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER, 1883, 60)

print("Cvor 2 pokrenut - saljem vlagu...")

while True:
    vlaga = round(random.uniform(40.0, 80.0), 1)
    poruka = str(vlaga)
    client.publish(TOPIC, poruka)
    print(f"Poslato: {vlaga}%")
    time.sleep(3)