import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
TOPIC = "iot/cvor1/temperatura"
CLIENT_ID = "cvor1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, CLIENT_ID)
client.connect(BROKER, 1883, 60)

print("Cvor 1 pokrenut - saljem temperaturu...")

while True:
    temperatura = round(random.uniform(18.0, 28.0), 1)
    poruka = str(temperatura)
    client.publish(TOPIC, poruka)
    print(f"Poslato: {temperatura}°C")
    time.sleep(3)