#include <Servo.h>
Servo servo;
int angle = 0;
int val = 0;

void setup() {
  servo.attach(12);
  servo.write(angle);
  Serial.begin(9600);
}

void loop() {
  val = analogRead(A0);  // read the input pin
  Serial.println(val);
  

  if (val>1000) {
    servo.write(90); 
  }

  if (val<1000) {
    servo.write(0);     
  }  
  delay(300);
}
