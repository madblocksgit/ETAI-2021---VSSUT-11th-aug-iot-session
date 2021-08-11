/***********************************
 * Target: Uploading Sensory Feed
 * Input:   DHT11
 * Output:  Raspberry Pi
 ***********************************/

#include "DHT.h"

DHT dht(2,DHT11);
 
void setup() {

  dht.begin();
  Serial.begin(9600);

}

void loop() {

  Serial.print("#"); // SOF
  Serial.print(","); // Seperator
  Serial.print(dht.readHumidity());
  Serial.print(",");
  Serial.print(dht.readTemperature());
  Serial.print(",");
  Serial.print("~"); // EOF
  Serial.println();
  delay(2000); // 2000ms - 2 seconds
  

}
