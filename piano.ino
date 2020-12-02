#include <LiquidCrystal.h>

LiquidCrystal lcd(24, 25, 26, 27, 28, 29);

int cnt = 0;
float highTime;

void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  pinMode(47, OUTPUT);
}

void loop()
{
  int Do = digitalRead(2);
  int Re = digitalRead(3);
  int Mi = digitalRead(4);
  int Fa = digitalRead(5);
  int Sol = digitalRead(6);
  int La = digitalRead(7);
  int Si = digitalRead(8);
  int _Do = digitalRead(9);
  int _Re = digitalRead(10);
  int _Fa = digitalRead(11);
  int _Sol = digitalRead(12);
  int _La = digitalRead(13);

  if (cnt == 4)
  {
    delay(1000);
    lcd.clear();
    cnt = 0;
  }

  if (Do == HIGH)
  {
    lcd.print("Do-");
    tone(47, 522, 500);
    delay(500);

    highTime = pulseIn(2, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('c');
    Serial.print(" \n");

    if (Do == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (Re == HIGH)
  {
    lcd.print("Re-");
    tone(47, 587, 500);
    delay(500);

    highTime = pulseIn(3, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('d');
    Serial.print(" \n");

    if (Re == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (Mi == HIGH)
  {
    lcd.print("Mi-");
    tone(47, 660, 500);
    delay(500);

    highTime = pulseIn(4, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('e');
    Serial.print(" \n");

    if (Mi == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (Fa == HIGH)
  {
    lcd.print("Fa-");
    tone(47, 699, 500);
    delay(500);

    highTime = pulseIn(5, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('f');
    Serial.print(" \n");

    if (Fa == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (Sol == HIGH)
  {
    lcd.print("Sol-");
    tone(47, 784, 500);
    delay(500);

    highTime = pulseIn(6, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('g');
    Serial.print(" \n");

    if (Sol == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (La == HIGH)
  {
    lcd.print("La-");
    tone(47, 880, 500);
    delay(500);

    highTime = pulseIn(7, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('a');
    Serial.print(" \n");

    if (La == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (Si == HIGH)
  {
    lcd.print("Si-");
    tone(47, 987, 500);
    delay(500);

    highTime = pulseIn(8, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print('b');
    Serial.print(" \n");

    if (Si == LOW)
    {
      noTone(47);
    }

    cnt++;
  }

  if (_Do == HIGH)
  {
    lcd.print("Do#-");
    tone(47, 554, 500);
    delay(500);

    highTime = pulseIn(9, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print("c#");
    Serial.print(" \n");

    if (_Do == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (_Re == HIGH)
  {
    lcd.print("Re#-");
    tone(47, 587, 500);
    delay(500);

    highTime = pulseIn(10, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print("d#");
    Serial.print(" \n");

    if (_Re == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (_Fa == HIGH)
  {
    lcd.print("Fa#-");
    tone(47, 740, 500);
    delay(500);

    highTime = pulseIn(11, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print("f#");
    Serial.print(" \n");

    if (_Fa == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (_Sol == HIGH)
  {
    lcd.print("Sol#-");
    tone(47, 830, 500);
    delay(500);

    highTime = pulseIn(12, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print("g#");
    Serial.print(" \n");

    if (_Sol == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
  if (_La == HIGH)
  {
    lcd.print("La#-");
    tone(47, 932, 500);
    delay(500);

    highTime = pulseIn(13, HIGH, 60000000) / 1000000.0;
    Serial.print(highTime, 1);
    Serial.print(" sec / ");
    Serial.print("a#");
    Serial.print(" \n");

    if (_La == LOW)
    {
      noTone(47);
    }

    cnt++;
  }
}