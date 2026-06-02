import paho.mqtt.client as mqtt
import sqlite3
from datetime import datetime

BROKER = "localhost"
BAZA = "merenja.db"

SENZORI = {
    "iot/cvor1/temperatura": {"naziv": "Temperatura", "jedinica": "C",   "min": 15,  "max": 30},
    "iot/cvor2/vlaga":       {"naziv": "Vlaga",       "jedinica": "%",   "min": 30,  "max": 70},
    "iot/cvor3/svetlost":    {"naziv": "Svetlost",    "jedinica": "lux", "min": 100, "max": 900},
}

statistika = {
    tema: {"broj": 0, "suma": 0.0, "min": None, "max": None}
    for tema in SENZORI
}


def init_baza():
    veza = sqlite3.connect(BAZA)
    veza.execute("""
        CREATE TABLE IF NOT EXISTS merenja (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            cvor      TEXT,
            velicina  TEXT,
            vrednost  REAL,
            jedinica  TEXT,
            status    TEXT,
            vreme     TEXT
        )
    """)
    veza.commit()
    return veza


def on_connect(client, userdata, flags, reason_code, properties):
    print("Server povezan na broker!")
    for tema in SENZORI:
        client.subscribe(tema)
        print(f"Pretplacen na: {tema}")


def on_message(client, userdata, msg):
    tema = msg.topic
    konfig = SENZORI[tema]
    vrednost = float(msg.payload.decode())

    s = statistika[tema]
    s["broj"] += 1
    s["suma"] += vrednost
    s["min"] = vrednost if s["min"] is None else min(s["min"], vrednost)
    s["max"] = vrednost if s["max"] is None else max(s["max"], vrednost)
    prosek = s["suma"] / s["broj"]

    if vrednost < konfig["min"] or vrednost > konfig["max"]:
        status = "ALARM"
        upozorenje = f"  !!! UPOZORENJE: van opsega ({konfig['min']}-{konfig['max']} {konfig['jedinica']})"
    else:
        status = "OK"
        upozorenje = ""

    vreme = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    userdata.execute(
        "INSERT INTO merenja (cvor, velicina, vrednost, jedinica, status, vreme) VALUES (?, ?, ?, ?, ?, ?)",
        (tema.split("/")[1], konfig["naziv"], vrednost, konfig["jedinica"], status, vreme),
    )
    userdata.commit()

    print(
        f"[{konfig['naziv']}] {vrednost} {konfig['jedinica']}  "
        f"(min={s['min']}, max={s['max']}, prosek={prosek:.1f}, n={s['broj']}){upozorenje}"
    )


baza = init_baza()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "server")
client.user_data_set(baza)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
print(f"Server pokrenut, podaci se cuvaju u '{BAZA}'. Cekam podatke...")
client.loop_forever()
