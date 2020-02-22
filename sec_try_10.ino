#include <CustomStepper.h>            // Подключаем библиотеку управления шаговым двигателем. По умолчанию настроена на двигатель 28BYJ-48-5V
#include <Ultrasonic.h>
Ultrasonic ultrasonic(4, 5);
CustomStepper stepper(8, 9, 10, 11);
void setup() {
  // put your setup code here, to run once:
  stepper.setRPM(12);                 // Устанавливаем кол-во оборотов в минуту
  stepper.setSPR(4075.7728395);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int distance = ultrasonic.read();
  if (distance < 10) {
    stepper.setDirection(STOP);
    Serial.println("1");
    delay(5000);
    if (Serial.available() > 0) {
    char ans = Serial.read();
    }
    stepper.setDirection(CW);
    stepper.rotate();
    stepper.run();
  } else {
    Serial.println("0");
    stepper.setDirection(CW);
    stepper.rotate();
    stepper.run();
  }
  //here we sort the garbage
}
