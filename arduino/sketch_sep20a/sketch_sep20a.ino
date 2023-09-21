const int pin13 = 13;


void setup() {
  Serial.begin(9600);
  pinMode(pin13, OUTPUT);
}

void loop() {
  if(Serial.available()>0){
    char caracter = Serial.read();
    if(caracter == 'e'){
      digitalWrite(pin13,HIGH);
    }
    if(caracter == 'a'){
      digitalWrite(pin13,LOW);
    }
  }
}
