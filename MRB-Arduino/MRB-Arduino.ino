//Specify digital pin on the Arduino that the positive lead of piezo buzzer is attached.
int piezoPin = 3;
unsigned int frequency=0;  // Max value is 65535
char incomingByte;

void setup() {
  Serial.begin(9600);
}//close setup
 
void loop() {
  if (Serial.available() > 0) {   // something came across serial
    frequency = 0;         // throw away previous integerValue
    while(1) {            // force into a loop until 'n' is received
      incomingByte = Serial.read();
      if (incomingByte == '\n') break;   // exit the while(1), we're done receiving
      if (incomingByte == -1) continue;  // if no characters are in the buffer read() returns -1
      frequency *= 10;  // shift left 1 decimal place
      // convert ASCII to integer, add, and shift left 1 decimal place
      frequency = ((incomingByte - 48) + frequency);
    }
    Serial.println(frequency);   // Do something with the value
  }
  tone(piezoPin, frequency, 500);
}