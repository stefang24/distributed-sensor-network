#include <DHT.h>

#define DHT_PIN  2
#define DHT_TYPE DHT11
#define POT_PIN  A0

DHT dht(DHT_PIN, DHT_TYPE);

float lastTemp  = 0;
float lastVlaga = 0;

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  if (!isnan(t)) lastTemp  = t;
  if (!isnan(h)) lastVlaga = h;

  int sirovo = analogRead(POT_PIN);
  long lux = map(sirovo, 0, 1023, 0, 1000);

  Serial.print(lastTemp);
  Serial.print(",");
  Serial.print(lastVlaga);
  Serial.print(",");
  Serial.println(lux);

  delay(3000);                          
}