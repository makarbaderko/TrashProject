#include <Ultrasonic.h>

Ultrasonic ultrasonic(12, 13);
int distance;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  String InBytes;
  // put your main code here, to run repeatedly:
  distance = ultrasonic.read();
  Serial.println(distance);
  delay(1000);
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil('\n');
    if (InBytes == "4") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("YES");
    } else {
    digitalWrite(LED_BUILTIN, LOW);
    Serial.write("NO");
   }
  }
}
