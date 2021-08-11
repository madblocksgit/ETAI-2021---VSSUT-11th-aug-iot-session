
/****************************************************************
 * Target: Control Relay (with Bulb) from AWS
 * 
 * Arduino is not having any internet connection
 * Raspberry Pi / Linux Desktop is having internect connection
 * 
 * Arduino is connected with USB Port of my Desktop
 * 
 * Input: Command from Rapsberry Pi
 * Output: Relay with Bulb
 ****************************************************************/

int relay=2; // bi-directional (both I&O)

void setup() {

  Serial.begin(9600); // initialising the Serial Port - 9600bps
  pinMode(relay,OUTPUT); // write permission
}

void loop() {

  // wait until rpi instructs command through USB (Serial)
  while(Serial.available()) { // on, off
    String s=Serial.readString();
    if(s=="on") {
      digitalWrite(relay,0); // bulb - on
    } else if(s=="off") {
      digitalWrite(relay,1); // bulb - off
    }
  }
  
}
