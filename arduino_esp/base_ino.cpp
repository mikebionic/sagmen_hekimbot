// #include <Ultrasonic.h>
#include <LiquidCrystal_I2C.h> 
#include <Wire.h> 
LiquidCrystal_I2C lcd(0x27, 16, 2);

int photoresistor_pin = A0;
int piezo = 6;

int red = 9;
int green = 10;
int blue = 11;

int but_acc_pin = 2;
int but_dec_pin = 3;
int but_acc_state;
int but_dec_state;

int photo_state = 0;
long x;
long y;
long clearDisp;
int clearedDisp = 0;

byte per[8] = 
{
  0b00100,
  0b00000,
  0b01110,
  0b10101,
  0b00100,
  0b01010,
  0b10001,
  0b00000
};

// Ultrasonic ultrasonic(A2,A3);

void setup() {
  Serial.begin(115200);
  lcd.begin();
  lcd.backlight();
  lcd.createChar(1, per);

  pinMode(photoresistor_pin, INPUT);
  // pinMode(piezo, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(but_acc_pin,INPUT);
  pinMode(but_dec_pin,INPUT);
  lcd.clear();
  lcd.setCursor (2,0);
  lcd.print("--HEKIMBOT--");


}

void display_show(String name,String title){
  if (photo_state < 40){
    clearDisp = millis();
    clearedDisp = 0;
    lcd.setCursor(2,0);
    lcd.print("Dogtor yok");
    lcd.setCursor(2,1);
    lcd.print("Garashylyar...");
    Serial.println("waiting");
    // delay(200);
  } else {
    lcd.clear();
    lcd.setCursor (0,0);
    lcd.write(1);
    lcd.setCursor (1,0);
    lcd.print(" " + name);
    lcd.setCursor (0,1);
    lcd.print("+ " + title);
  }
}


void loop() {
  photoresistor();
  if (clearDisp + 6000 < millis() && clearedDisp == 0){
    lcd.clear();
    lcd.setCursor (2,0);
    lcd.print("--HEKIMBOT--");
    clearedDisp = 1;
  }
  but_acc_state = digitalRead(but_acc_pin);
  but_dec_state = digitalRead(but_dec_pin);
   if (but_acc_state > 0){
    clearDisp = millis();
    clearedDisp = 0;
    lcd.clear();
    lcd.setCursor (0,0);
    lcd.print("Kabul edildi!");
    Serial.println("accepted");
    y = millis();
    signal_send_msg();
   }
   if (but_dec_state > 0){
    clearDisp = millis();
    clearedDisp = 0;
    lcd.clear();
    lcd.setCursor (0,0);
    lcd.print("Terk edildi!");
    Serial.println("declined");
    y = millis();
    signal_send_msg();
   }

  if (Serial.available() != 0) {
    String stream = Serial.readStringUntil('\n');
    stream.trim();
    lcd.clear();
    if (stream.length() > 0) {
      String name = getStringPartByDelimeter(stream, ':', 0);
      String title = getStringPartByDelimeter(stream, ':', 1);
      clearDisp = millis();
      clearedDisp = 0;
      display_show(name, title);
      x = millis();
      signal_new_msg();
    }
  }
}


void photoresistor(){
  photo_state = analogRead(photoresistor_pin);
  // Serial.print("Photo: ");
  // Serial.println(photo_state);
}

void sound() {
  if (x+400 < millis()){
    tone(piezo, 500);
    if (x+800 < millis()){
      noTone(piezo);
      x = millis();
    }
  }
}

void signal_new_msg() {

  tone(piezo, 1200);
  digitalWrite(red,1);
  delay(200);
  noTone(piezo);
  digitalWrite(red,0);
  delay(200);
  tone(piezo, 1200);
  digitalWrite(red,1);
  delay(200);
  noTone(piezo);
  digitalWrite(red,0);
  // delay(200);
  // while(x + 1001 < millis()){

  //   if (x+200 < millis()){
  //     tone(piezo, 1200);
  //     digitalWrite(red,1);
  //   }
  //   if (x+400 < millis()){
  //     noTone(piezo);
  //     digitalWrite(red,0);
  //   }
    // if (x+800 < millis()){
    //   tone(piezo, 1200);
    //   digitalWrite(red,1);
    // }
    // if (x+1000 < millis()){
    //   noTone(piezo);
    //   digitalWrite(red,0);
    // }
  // }
}

void signal_send_msg() {

  tone(piezo, 800);
  digitalWrite(red,1);
  delay(500);
  noTone(piezo);
  digitalWrite(red,0);
  
  // while (y + 1001 < millis()) {

  //   Serial.println("start");
  //   if (y+500 < millis()){
  //     Serial.println("tone");
  //     tone(piezo, 800);
  //     digitalWrite(red,1);
  //   }
  //   if (y+1000 < millis()){
  //     Serial.println("notone");
  //     noTone(piezo);
  //     digitalWrite(red,0);
  //   }
  // }
}


void led_c() {
  digitalWrite(red,1);
  digitalWrite(green,0);
  digitalWrite(blue,0);
  delay(1000);
  digitalWrite(red,0);
  digitalWrite(green,1);
  digitalWrite(blue,0);
  delay(1000);
  digitalWrite(red,0);
  digitalWrite(green,0);
  digitalWrite(blue,1);
  delay(1000);  
}




////////////////////////////////////////////



String getStringPartByDelimeter(String data, char separator, int index) {
  int stringData = 0;
  String dataPart = "";
  for (int i = 0; i < data.length() - 1; i++) {
    if (data[i] == separator) {
      stringData++;
    } else if (stringData == index) {
      dataPart.concat(data[i]);
    } else if (stringData > index) {
      return dataPart;
      break;
    }
  }
  return dataPart;
}
