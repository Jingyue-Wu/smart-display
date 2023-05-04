#include <LiquidCrystal.h>
const int rs = 2, en = 3, d4 = 4, d5 = 5, d6 = 6, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const int green = 9;
const int red = 10;

int data;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  pinMode(green, OUTPUT);
  pinMode(red, OUTPUT);
}

void loop() {
  while (Serial.available() > 0) {
    data = Serial.read();
    if (data == '{') {
      digitalWrite(green, HIGH);
      digitalWrite(red, LOW);
    }
    else if (data == '}') {
      digitalWrite(green, LOW);
      digitalWrite(red, HIGH);
    }
    else if (data == '/') {
      lcd.clear();
    }
    else if (data == '[') {
      lcd.setCursor(0, 0);
    }
    else if (data == ']') {
      lcd.setCursor(0, 1);
    }
    else {
        lcd.write(data);
    }
  }
}
