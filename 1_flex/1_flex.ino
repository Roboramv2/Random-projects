int val = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  val = analogRead(A0);  // read the input pin
  Serial.println(val);
  delay(300);
}
