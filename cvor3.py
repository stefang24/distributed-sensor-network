import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "iot/cvor3/svetlost"
CLIENT_ID = "cvor3"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER, 1883, 60)

print("Cvor 3 pokrenut - saljem svetlost...")

while True:
    svetlost = round(random.uniform(100.0, 1000.0), 1)
    poruka = str(svetlost)
    client.publish(TOPIC, poruka)
    print(f"Poslato: {svetlost} lux")
    time.sleep(3)