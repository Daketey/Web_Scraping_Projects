#include<Servo.h>

Servo serX;
String serialData;

void setup() {
  serX.attach(10);
  Serial.begin(9600);
  Serial.setTimeout(10);
  serX.write(0);       
}

void loop() {
  //lmao

}

void serialEvent() {
  serialData = Serial.readString();
  serX.write(parseDataX(serialData));
}

int parseDataX(String data){
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}
