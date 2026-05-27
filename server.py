import paho.mqtt.client as mqtt

BROKER = "localhost"
TOPICS = [
    "iot/cvor1/temperatura",
    "iot/cvor2/vlaga",
    "iot/cvor3/svetlost"
]

def on_connect(client, userdata, flags, reason_code, properties):
    print("Server povezan na broker!")
    for topic in TOPICS:
        client.subscribe(topic)
        print(f"Pretplacen na: {topic}")

def on_message(client, userdata, msg):
    tema = msg.topic
    vrednost = msg.payload.decode()
    
    if "temperatura" in tema:
        print(f"[CVOR 1] Temperatura: {vrednost} C")
    elif "vlaga" in tema:
        print(f"[CVOR 2] Vlaga: {vrednost} %")
    elif "svetlost" in tema:
        print(f"[CVOR 3] Svetlost: {vrednost} lux")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "server")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
print("Server pokrenut, cekam podatke...")
client.loop_forever()