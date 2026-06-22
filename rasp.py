import serial
import paho.mqtt.client as mqtt

BROKER = "192.168.1.5"
PORT   = "/dev/ttyACM0"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "rasp")
client.connect(BROKER, 1883, 60)
client.loop_start()

ser = serial.Serial(PORT, 9600, timeout=5)
print(f"Cvor pokrenut - citam Arduino sa {PORT} i saljem na MQTT...")

while True:
    linija = ser.readline().decode(errors="ignore").strip()
    if not linija:
        continue
    try:
        temperatura, vlaga, svetlost = linija.split(",")
        client.publish("iot/cvor1/temperatura", temperatura)
        client.publish("iot/cvor2/vlaga", vlaga)
        client.publish("iot/cvor3/svetlost", svetlost)
        print(f"Poslato -> temp:{temperatura}C vlaga:{vlaga}% svetlost:{svetlost}lux")
    except ValueError:
        pass