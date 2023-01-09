const int green_pin = 8;


void setup() {
  Serial.begin(115200);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);

}

void loop() {
int serial_data;

//serial_data = Serial.readString().toInt();
serial_data = Serial.read();

while(Serial.available() ==0){
  if (serial_data == '6'){
    digitalWrite(2,HIGH);
    //Serial.println("on");
    delay(100);
    Serial.println("Green");
    digitalWrite(2,LOW);
    break;
  }
  else if(serial_data =='7'){
    digitalWrite(3,HIGH);
    //Serial.println("on");
    delay(100);
    Serial.println("Red");
    digitalWrite(3,LOW);
    break;
   // delayMicroseconds(1000);
 // }
}
  else if(serial_data =='8'){
    digitalWrite(4,HIGH);
    //Serial.println("on");
    delay(100);
    Serial.println("Yellow");
    digitalWrite(4,LOW);
    break;
}
}
}
