const int op1 = 2, op2 = 3, op3 = 4, op4 = 5;
const int ledPin =  13;

int op1State = 0, op2State = 0, op3State = 0, op4State = 0;
bool pressed = false;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(op1, INPUT);
  pinMode(op2, INPUT);
  pinMode(op3, INPUT);
  pinMode(op4, INPUT);
}

void loop() {
  read_buttons();
  is_pressed();
}

char send_op(){
  if(op1State == HIGH){
    return '1';
  }
  else if(op2State == HIGH){
    return '2';
  }
  else if(op3State == HIGH){
    return '3';
  }
  else if(op4State == HIGH){
    return '4';
  }
  else{
    return '0';
  }
}

void read_buttons(){
  op1State = digitalRead(op1);
  op2State = digitalRead(op2);
  op3State = digitalRead(op3);
  op4State = digitalRead(op4);
}
void is_pressed(){
  if(op1State == HIGH || op2State == HIGH || op3State == HIGH || op4State == HIGH){
    digitalWrite(ledPin, HIGH);
    Serial.println(send_op());
  }else{
    digitalWrite(ledPin, LOW);
  }
}
