void setup() {
  // put your setup code here, to run once:
  Serial.begin(119200);
  pinMode(3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    byte command = Serial.read();
    if(command == '0') {
      digitalWrite(3, LOW);
    } else if (command == '1') {
      digitalWrite(3, HIGH);
    }
  }
}
