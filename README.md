# IoT Distribuirani Senzorski Cvor

Simulacija distribuiranog IoT sistema sa 3 senzorska cvora koji mere temperaturu, vlagu i svetlost i prikazuju podatke u realnom vremenu na web dashboardu.

## Sta sistem radi

- 3 virtuelna cvora salju podatke (temperatura, vlaga, svetlost) putem MQTT protokola
- Mosquitto MQTT broker prima i prosledjuje podatke
- Node-RED dashboard prikazuje podatke u realnom vremenu sa gauge-ovima i grafovima

## Arhitektura

```
[cvor1.py] --\
[cvor2.py] ----> [Mosquitto MQTT Broker] --> [Node-RED Dashboard]
[cvor3.py] --/
```

---

## Instalacija

### 1. Python

Preuzmi sa https://www.python.org/downloads/ i instaliraj.

> VAZNO: Pri instalaciji obavezno stikliraj "Add Python to PATH"

Proveri instalaciju:
```
python --version
```

Instaliraj potrebne biblioteke:
```
pip install paho-mqtt
```

---

### 2. Mosquitto MQTT Broker

Preuzmi sa https://mosquitto.org/download/ (Windows .exe verzija) i instaliraj.

Dodaj Mosquitto u PATH:
- Windows taster -> ukucaj "environment variables" -> Edit the system environment variables
- Environment Variables -> System variables -> Path -> Edit -> New
- Dodaj: `C:\Program Files\mosquitto`
- Klikni OK na svim prozorima

Proveri instalaciju (novi cmd):
```
mosquitto -v
```

Mosquitto se automatski pokrace kao Windows servis pri svakom pokretanju racunara.

---

### 3. Node.js

Preuzmi sa https://nodejs.org/ (LTS verziju) i instaliraj.

Proveri instalaciju:
```
node --version
```

---

### 4. Node-RED

Instaliraj putem npm:
```
npm install -g --unsafe-perm node-red
```

Proveri instalaciju:
```
node-red --version
```

---

### 5. Node-RED Dashboard plugin

Pokreni Node-RED:
```
node-red
```

Otvori browser na http://localhost:1880

Idi na: hamburger meni (gore desno) -> Manage palette -> Install

U search ukucaj `@flowfuse/node-red-dashboard` i klikni Install.

---

## Pokretanje projekta

### Korak 1 - Pokreni Node-RED
```
node-red
```

### Korak 2 - Importuj dashboard

- Otvori http://localhost:1880
- Hamburger meni -> Import
- Ucitaj flows.json fajl
- Klikni Deploy (crveno dugme gore desno)

### Korak 3 - Pokreni senzorske cvorove

Otvori 3 zasebna cmd prozora i u svakom naviguj do foldera projekta:
```
cd putanja\do\foldera
```

Pa pokreni svaki cvor u svom prozoru:
```
python cvor1.py
```
```
python cvor2.py
```
```
python cvor3.py
```

### Korak 4 - Otvori dashboard

```
http://localhost:1880/dashboard
```

---

## Struktura projekta

```
IoT_projekat/
├── flows.json      - Node-RED dashboard konfiguracija
├── cvor1.py        - Simulacija cvora 1 (temperatura)
├── cvor2.py        - Simulacija cvora 2 (vlaga)
├── cvor3.py        - Simulacija cvora 3 (svetlost)
├── server.py       - MQTT server za debug ispis u konzoli
├── requirements.txt - Python zavisnosti
└── README.md       - Ovo uputstvo
```

---

## Resavanje problema

**mosquitto nije prepoznat kao komanda:**
Proveri da li je dodat u PATH (vidi korak 2)

**pip install ne radi:**
Pokusaj sa:
```
python -m pip install paho-mqtt
```

**Dashboard ne prikazuje podatke:**
- Proveri da li su pokrenuti svi cvorovi (cvor1.py, cvor2.py, cvor3.py)
- Proveri da li je Mosquitto pokrenut
- U Node-RED editoru proveri da li pise "connected" ispod MQTT cvorova

---

## Tim

- Stefan Grujicic - 40/2022
- Mateja Planic - 81/2022
- Mihailo Obradovic - 79/2022
- Aleksandar Golubovic - 43/2022

## Predmet

Internet of Things (IoT) - [NAZIV FAKULTETA], 2026.
