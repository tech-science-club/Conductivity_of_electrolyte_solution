#include <Wire.h>
#include <Stepper.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x3F for a 16 chars and 2 line display

int stepCount = 0;
int analogPin = 0;
int volts = 1;
int raw = 0;
int V = 0;
float Vin = 3.3;
float Vout = 0;
float R1 = 1000;
float R2 = 0;
float buffer = 0;
float conductivity;
const int rpm = 10;

void setup(){
  lcd.init();
  lcd.clear();         
  lcd.backlight();
  Serial.begin(9600);
}

void loop(){
  raw = analogRead(analogPin);
  
  if(raw){
    buffer = raw * Vin;
    Vout = (buffer)/1024.0;
    buffer = (Vin/Vout) - 1;
    R2 = R1 * buffer;
    conductivity = 1/R2*100;
    
    lcd.setCursor(0, 0);
    lcd.print("V out: ");
    lcd.print(Vout);

    lcd.setCursor(0, 1);
    lcd.print("Cnd: ");
    lcd.print(conductivity, 6);
    
    Serial.print("Cnd: ");
    Serial.println(conductivity, 6);
    delay(1000);
  }

}
