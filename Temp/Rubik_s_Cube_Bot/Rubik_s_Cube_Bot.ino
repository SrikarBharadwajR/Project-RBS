

#include <iostream>
#include <Arduino.h>

String whiteArray[9] =  {"g", "g", "g", "b", "w", "o", "b", "g", "w"};
String yellowArray[9] = {"g", "o", "w", "w", "y", "r", "r", "y", "b"};
String redArray[9] =    {"y", "w", "b", "g", "r", "g", "y", "b", "r"};
String orangeArray[9] = {"o", "r", "o", "b", "o", "o", "y", "r", "w"};
String blueArray[9] =   {"o", "w", "w", "o", "b", "y", "g", "b", "o"};
String greenArray[9] =  {"y", "w", "r", "y", "g", "y", "b", "r", "r"};

void WhiteMotorClk()
{
  digitalWrite(1, HIGH);
  delay(10);
  digitalWrite(1, LOW);
  String newwhiteArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newredArray[0] = blueArray[0];
  newredArray[1] = blueArray[1];
  newredArray[2] = blueArray[2];
  newblueArray[0] = orangeArray[0];
  newblueArray[1] = orangeArray[1];
  newblueArray[2] = orangeArray[2];
  neworangeArray[0] = greenArray[0];
  neworangeArray[1] = greenArray[1];
  neworangeArray[2] = greenArray[2];
  newgreenArray[0] = redArray[0];
  newgreenArray[1] = redArray[1];
  newgreenArray[2] = redArray[2];
  newwhiteArray[2] = whiteArray[0];
  newwhiteArray[5] = whiteArray[1];
  newwhiteArray[8] = whiteArray[2];
  newwhiteArray[1] = whiteArray[3];
  newwhiteArray[7] = whiteArray[5];
  newwhiteArray[0] = whiteArray[6];
  newwhiteArray[3] = whiteArray[7];
  newwhiteArray[6] = whiteArray[8];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("White Motor Turned ClockWise");
}
void WhiteMotorAClk()
{
  digitalWrite(7, HIGH);
  delay(10);
  digitalWrite(7, LOW);
  String newwhiteArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newblueArray[0] = redArray[0];
  newblueArray[1] = redArray[1];
  newblueArray[2] = redArray[2];
  newredArray[0] = greenArray[0];
  newredArray[1] = greenArray[1];
  newredArray[2] = greenArray[2];
  newgreenArray[0] = orangeArray[0];
  newgreenArray[1] = orangeArray[1];
  newgreenArray[2] = orangeArray[2];
  neworangeArray[0] = blueArray[0];
  neworangeArray[1] = blueArray[1];
  neworangeArray[2] = blueArray[2];
  newwhiteArray[0] = whiteArray[2];
  newwhiteArray[1] = whiteArray[5];
  newwhiteArray[2] = whiteArray[8];
  newwhiteArray[3] = whiteArray[1];
  newwhiteArray[5] = whiteArray[7];
  newwhiteArray[6] = whiteArray[0];
  newwhiteArray[7] = whiteArray[3];
  newwhiteArray[8] = whiteArray[6];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("White Motor Turned Anti ClockWise");
}
void YellowMotorClk()
{
  digitalWrite(2, HIGH);
  delay(10);
  digitalWrite(2, LOW);
  String newyellowArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newblueArray[6] = redArray[6];
  newblueArray[7] = redArray[7];
  newblueArray[8] = redArray[8];
  newredArray[6] = greenArray[6];
  newredArray[7] = greenArray[7];
  redArray[8] = greenArray[8];
  newgreenArray[6] = orangeArray[6];
  newgreenArray[7] = orangeArray[7];
  newgreenArray[8] = orangeArray[8];
  neworangeArray[6] = blueArray[6];
  neworangeArray[7] = blueArray[7];
  neworangeArray[8] = blueArray[8];
  newyellowArray[2] = yellowArray[0];
  newyellowArray[5] = yellowArray[1];
  newyellowArray[8] = yellowArray[2];
  newyellowArray[1] = yellowArray[3];
  newyellowArray[7] = yellowArray[5];
  newyellowArray[0] = yellowArray[6];
  newyellowArray[3] = yellowArray[7];
  newyellowArray[6] = yellowArray[8];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Yellow Motor Turned ClockWise");
}
void YellowMotorAClk()
{
  digitalWrite(8, HIGH);
  delay(10);
  digitalWrite(8, LOW);
  String newyellowArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newredArray[6] = blueArray[6];
  newredArray[7] = blueArray[7];
  newredArray[8] = blueArray[8];
  newblueArray[6] = orangeArray[6];
  newblueArray[7] = orangeArray[7];
  newblueArray[8] = orangeArray[8];
  neworangeArray[6] = greenArray[6];
  neworangeArray[7] = greenArray[7];
  neworangeArray[8] = greenArray[8];
  newgreenArray[6] = redArray[6];
  newgreenArray[7] = redArray[7];
  newgreenArray[8] = redArray[8];
  newyellowArray[0] = yellowArray[2];
  newyellowArray[1] = yellowArray[5];
  newyellowArray[2] = yellowArray[8];
  newyellowArray[3] = yellowArray[1];
  newyellowArray[5] = yellowArray[7];
  newyellowArray[6] = yellowArray[0];
  newyellowArray[7] = yellowArray[3];
  newyellowArray[8] = yellowArray[6];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Yellow Motor Turned Anti ClockWise");
}
void RedMotorClk()
{
  digitalWrite(3, HIGH);
  delay(10);
  digitalWrite(3, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String newredArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newblueArray[0] = whiteArray[6];
  newblueArray[3] = whiteArray[7];
  newblueArray[6] = whiteArray[8];
  newyellowArray[2] = blueArray[0];
  newyellowArray[1] = blueArray[3];
  newyellowArray[0] = blueArray[6];
  newgreenArray[2] = yellowArray[0];
  newgreenArray[5] = yellowArray[1];
  newgreenArray[8] = yellowArray[2];
  newwhiteArray[8] = greenArray[2];
  newwhiteArray[7] = greenArray[5];
  newwhiteArray[6] = greenArray[8];
  newredArray[2] = redArray[0];
  newredArray[5] = redArray[1];
  newredArray[8] = redArray[2];
  newredArray[1] = redArray[3];
  newredArray[7] = redArray[5];
  newredArray[0] = redArray[6];
  newredArray[3] = redArray[7];
  newredArray[6] = redArray[8];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Red Motor Turned ClockWise");
}
void RedMotorAClk()
{
  digitalWrite(9, HIGH);
  delay(10);
  digitalWrite(9, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String newredArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newwhiteArray[6] = blueArray[0];
  newwhiteArray[7] = blueArray[3];
  newwhiteArray[8] = blueArray[6];
  newblueArray[0] = yellowArray[2];
  newblueArray[3] = yellowArray[1];
  newblueArray[6] = yellowArray[0];
  newyellowArray[0] = greenArray[2];
  newyellowArray[1] = greenArray[5];
  newyellowArray[2] = greenArray[8];
  newgreenArray[2] = whiteArray[8];
  newgreenArray[5] = whiteArray[7];
  newgreenArray[8] = whiteArray[6];
  newredArray[0] = redArray[2];
  newredArray[1] = redArray[5];
  newredArray[2] = redArray[8];
  newredArray[3] = redArray[1];
  newredArray[5] = redArray[7];
  newredArray[6] = redArray[0];
  newredArray[7] = redArray[3];
  newredArray[8] = redArray[6];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Red Motor Turned Anti ClockWise");
}
void OrangeMotorClk()
{
  digitalWrite(4, HIGH);
  delay(10);
  digitalWrite(4, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newwhiteArray[0] = blueArray[2];
  newwhiteArray[1] = blueArray[5];include <iostream>

  newwhiteArray[2] = blueArray[8];
  newblueArray[8] = yellowArray[6];
  newblueArray[5] = yellowArray[7];
  newblueArray[2] = yellowArray[8];
  newyellowArray[6] = greenArray[0];
  newyellowArray[7] = greenArray[3];
  newyellowArray[8] = greenArray[6];
  newgreenArray[0] = whiteArray[2];
  newgreenArray[3] = whiteArray[1];
  newgreenArray[6] = whiteArray[0];
  neworangeArray[2] = orangeArray[0];
  neworangeArray[5] = orangeArray[1];
  neworangeArray[8] = orangeArray[2];
  neworangeArray[1] = orangeArray[3];
  neworangeArray[7] = orangeArray[5];
  neworangeArray[0] = orangeArray[6];
  neworangeArray[3] = orangeArray[7];
  neworangeArray[6] = orangeArray[8];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Orange Motor Turned ClockWise");
}
void OrangeMotorAClk()
{
  digitalWrite(10, HIGH);
  delay(10);
  digitalWrite(10, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  String newgreenArray[9];
  newblueArray[2] = whiteArray[0];
  newblueArray[5] = whiteArray[1];
  newblueArray[8] = whiteArray[2];
  newyellowArray[6] = blueArray[8];
  newyellowArray[7] = blueArray[5];
  newyellowArray[8] = blueArray[2];
  newgreenArray[0] = yellowArray[6];
  newgreenArray[3] = yellowArray[7];
  newgreenArray[6] = yellowArray[8];
  newwhiteArray[2] = greenArray[0];
  newwhiteArray[1] = greenArray[3];
  newwhiteArray[0] = greenArray[6];
  neworangeArray[0] = orangeArray[2];
  neworangeArray[1] = orangeArray[5];
  neworangeArray[2] = orangeArray[8];
  neworangeArray[3] = orangeArray[1];
  neworangeArray[5] = orangeArray[7];
  neworangeArray[6] = orangeArray[0];
  neworangeArray[7] = orangeArray[3];
  neworangeArray[8] = orangeArray[6];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Orange Motor Turned Anti ClockWise");
}
void BlueMotorClk()
{
  digitalWrite(5, HIGH);
  delay(10);
  digitalWrite(5, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  newwhiteArray[2] = redArray[2];
  newwhiteArray[5] = redArray[5];
  newwhiteArray[8] = redArray[8];
  newredArray[2] = yellowArray[2];
  newredArray[5] = yellowArray[5];
  newredArray[8] = yellowArray[8];
  newyellowArray[2] = orangeArray[0];
  newyellowArray[5] = orangeArray[3];
  newyellowArray[8] = orangeArray[6];
  neworangeArray[0] = whiteArray[8];
  neworangeArray[3] = whiteArray[5];
  neworangeArray[6] = whiteArray[2];
  newblueArray[2] = blueArray[0];
  newblueArray[5] = blueArray[1];
  newblueArray[8] = blueArray[2];
  newblueArray[1] = blueArray[3];
  newblueArray[7] = blueArray[5];
  newblueArray[0] = blueArray[6];
  newblueArray[3] = blueArray[7];
  newblueArray[6] = blueArray[8];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  Serial.println("Blue Motor Turned ClockWise");
}
void BlueMotorAClk()
{
  digitalWrite(11, HIGH);
  delay(10);
  digitalWrite(11, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newblueArray[9];
  newwhiteArray[8] = orangeArray[0];
  newwhiteArray[5] = orangeArray[3];
  newwhiteArray[2] = orangeArray[6];
  neworangeArray[0] = yellowArray[2];
  neworangeArray[3] = yellowArray[5];
  neworangeArray[6] = yellowArray[8];
  newyellowArray[2] = redArray[2];
  newyellowArray[5] = redArray[5];
  newyellowArray[8] = redArray[8];
  newredArray[2] = whiteArray[2];
  newredArray[5] = whiteArray[5];
  newredArray[8] = whiteArray[8];
  newyellowArray[0] = yellowArray[2];
  newyellowArray[1] = yellowArray[5];
  newyellowArray[2] = yellowArray[8];
  newyellowArray[3] = yellowArray[1];
  newyellowArray[5] = yellowArray[7];
  newyellowArray[6] = yellowArray[0];
  newyellowArray[7] = yellowArray[3];
  newyellowArray[8] = yellowArray[6];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newblueArray[i] != "")
      blueArray[i] = newblueArray[i];
  Serial.println("Blue Motor Turned Anti ClockWise");
}
void GreenMotorClk()
{
  digitalWrite(6, HIGH);
  delay(10);
  digitalWrite(6, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newgreenArray[9];
  newwhiteArray[0] = orangeArray[8];
  newwhiteArray[3] = orangeArray[5];
  newwhiteArray[6] = orangeArray[2];
  neworangeArray[8] = yellowArray[0];
  neworangeArray[5] = yellowArray[3];
  neworangeArray[2] = yellowArray[6];
  newyellowArray[0] = redArray[0];
  newyellowArray[3] = redArray[3];
  newyellowArray[6] = redArray[6];
  newredArray[0] = whiteArray[0];
  newredArray[3] = whiteArray[3];
  newredArray[6] = whiteArray[6];
  newgreenArray[2] = greenArray[0];
  newgreenArray[5] = greenArray[1];
  newgreenArray[8] = greenArray[2];
  newgreenArray[1] = greenArray[3];
  newgreenArray[7] = greenArray[5];
  newgreenArray[0] = greenArray[6];
  newgreenArray[3] = greenArray[7];
  newgreenArray[6] = greenArray[8];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Green Motor Turned ClockWise");
}
void GreenMotorAClk()
{
  digitalWrite(12, HIGH);
  delay(10);
  digitalWrite(12, LOW);
  String newwhiteArray[9];
  String newyellowArray[9];
  String newredArray[9];
  String neworangeArray[9];
  String newgreenArray[9];
  newwhiteArray[0] = redArray[0];
  newwhiteArray[3] = redArray[3];
  newwhiteArray[6] = redArray[6];
  newredArray[0] = yellowArray[0];
  newredArray[3] = yellowArray[3];
  newredArray[6] = yellowArray[6];
  newyellowArray[0] = orangeArray[8];
  newyellowArray[3] = orangeArray[5];
  newyellowArray[6] = orangeArray[2];
  neworangeArray[8] = whiteArray[0];
  neworangeArray[5] = whiteArray[3];
  neworangeArray[2] = whiteArray[6];
  newgreenArray[0] = greenArray[2];
  newgreenArray[1] = greenArray[5];
  newgreenArray[2] = greenArray[8];
  newgreenArray[3] = greenArray[1];
  newgreenArray[5] = greenArray[7];
  newgreenArray[6] = greenArray[0];
  newgreenArray[7] = greenArray[3];
  newgreenArray[8] = greenArray[6];
  for (int i = 0; i < 9; i++)
    if (newwhiteArray[i] != "")
      whiteArray[i] = newwhiteArray[i];
  for (int i = 0; i < 9; i++)
    if (newyellowArray[i] != "")
      yellowArray[i] = newyellowArray[i];
  for (int i = 0; i < 9; i++)
    if (newredArray[i] != "")
      redArray[i] = newredArray[i];
  for (int i = 0; i < 9; i++)
    if (neworangeArray[i] != "")
      orangeArray[i] = neworangeArray[i];
  for (int i = 0; i < 9; i++)
    if (newgreenArray[i] != "")
      greenArray[i] = newgreenArray[i];
  Serial.println("Green Motor Turned Anti ClockWise");
}
void setup()
{
  Serial.begin(9600);
  //ClockWise Pins
  pinMode(1, OUTPUT);//White should always be in top for R,O,B,G
  pinMode(2, OUTPUT);//Yellow
  pinMode(3, OUTPUT);//Red should always be in top for Y and facing towards you while measuring white
  pinMode(4, OUTPUT);//Orange
  pinMode(5, OUTPUT);//Blue
  pinMode(6, OUTPUT);//Green
  //Anticlockwise Pins
  pinMode(7, OUTPUT);//White
  pinMode(8, OUTPUT);//Yellow
  pinMode(9, OUTPUT);//Red
  pinMode(10, OUTPUT);//Orange
  pinMode(11, OUTPUT);//Blue
  pinMode(12, OUTPUT);//Green
  // for White Cross
  // for White Red piece
  //search white piece in white face
  if (whiteArray[1] == "w" && orangeArray[1] == "r")
  {
    WhiteMotorClk();
    WhiteMotorClk();
  }
  if (whiteArray[5] == "w" && blueArray[1] == "r")
  {
    WhiteMotorClk();
  }
  if (whiteArray[3] == "w" && greenArray[1] == "r")
  {
    WhiteMotorAClk();
  }
  //search white piece in yellow face
  if (yellowArray[1] == "w" && redArray[7] == "r")
  {
    RedMotorClk();
    RedMotorClk();
  }
  if (yellowArray[7] == "w" && orangeArray[7] == "r")
  {
    YellowMotorClk();
    YellowMotorClk();
    RedMotorClk();
    RedMotorClk();
  }
  if (yellowArray[5] == "w" && blueArray[7] == "r")
  {
    YellowMotorAClk();
    RedMotorClk();
    RedMotorClk();
  }
  if (yellowArray[3] == "w" && greenArray[7] == "r")
  {
    YellowMotorClk();
    RedMotorClk();
    RedMotorClk();
  }
  //search white piece in red face
  if (redArray[1] == "w" && whiteArray[7] == "r")
  {
    RedMotorClk();
    BlueMotorAClk();
    YellowMotorAClk();
    RedMotorAClk();
    RedMotorAClk();
  }
  if (redArray[3] == "w" && greenArray[5] == "r")
  {
    GreenMotorClk();
    YellowMotorClk();
    RedMotorAClk();
    RedMotorAClk();
  }
  if (redArray[5] == "w" && blueArray[3] == "r")
  {
    BlueMotorAClk();
    YellowMotorAClk();
    RedMotorAClk();
    RedMotorAClk();
  }
  if (redArray[7] == "w" && yellowArray[1] == "r")
  {
    YellowMotorAClk();
    GreenMotorAClk();
    RedMotorClk();
  }
  //search white piece in orange face

  if (orangeArray[1] == "w" && whiteArray[1] == "r")
  {
    OrangeMotorAClk();
    BlueMotorClk();
    YellowMotorAClk();
    RedMotorClk();
    RedMotorClk();
  }
  if (orangeArray[3] == "w" && blueArray[5] == "r")
  {
    BlueMotorClk();
    YellowMotorAClk();
    RedMotorClk();
    RedMotorClk();
  }
  if (orangeArray[5] == "w" && greenArray[3] == "r")
  {
    GreenMotorAClk();
    YellowMotorClk();
    RedMotorClk();
    RedMotorClk();
  }
  if (orangeArray[7] == "w" && yellowArray[7] == "r")
  {
    OrangeMotorClk();
    BlueMotorClk();
    YellowMotorAClk();
    RedMotorClk();
    RedMotorClk();
  }
  //search white piece in blue face
  if (blueArray[1] == "w" && whiteArray[5] == "r")
  {
    BlueMotorAClk();
    RedMotorAClk();
  }
  if (blueArray[3] == "w" && redArray[5] == "r")
  {
    RedMotorAClk();
  }
  if (blueArray[5] == "w" && orangeArray[3] == "r")
  {
    BlueMotorClk();
    BlueMotorClk();
    RedMotorAClk();
  }
  if (blueArray[7] == "w" && yellowArray[5] == "r")
  {
    BlueMotorClk();
    RedMotorAClk();
  }

  //search white piece in green face
  if (greenArray[1] == "w" && whiteArray[3] == "r")
  {
    GreenMotorClk();
    RedMotorClk();
  }
  if (greenArray[3] == "w" && orangeArray[5] == "r")
  {
    GreenMotorAClk();
    GreenMotorAClk();
    RedMotorClk();
  }
  if (greenArray[5] == "w" && redArray[3] == "r")
  {
    RedMotorClk();
  }
  if (greenArray[7] == "w" && yellowArray[3] == "r")
  {
    GreenMotorAClk();
    RedMotorClk();
  }
  // for White Orange piece
  //search white piece in white face
  if (whiteArray[5] == "w" && blueArray[1] == "o")
  {
    BlueMotorAClk();
    BlueMotorAClk();
    YellowMotorClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (whiteArray[3] == "w" && greenArray[1] == "o")
  {
    GreenMotorAClk();
    GreenMotorAClk();
    YellowMotorAClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  //search white piece in yellow face
  if (yellowArray[1] == "w" && redArray[7] == "o")
  {
    YellowMotorAClk();
    YellowMotorAClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (yellowArray[7] == "w" && orangeArray[7] == "o")
  {
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (yellowArray[5] == "w" && blueArray[7] == "o")
  {
    YellowMotorClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (yellowArray[3] == "w" && greenArray[7] == "o")
  {
    YellowMotorAClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  //search white piece in red face
  if (redArray[3] == "w" && greenArray[5] == "o")
  {
    GreenMotorClk();
    YellowMotorAClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (redArray[5] == "w" && blueArray[3] == "o")
  {
    BlueMotorAClk();
    YellowMotorClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (redArray[7] == "w" && yellowArray[1] == "o")
  {
    YellowMotorClk();
    BlueMotorAClk();
    OrangeMotorClk();
  }
  //search white piece in orange face

  if (orangeArray[1] == "w" && whiteArray[1] == "o")
  {
    OrangeMotorAClk();
    BlueMotorClk();
    YellowMotorClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (orangeArray[3] == "w" && blueArray[5] == "o")
  {
    BlueMotorClk();
    YellowMotorClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (orangeArray[5] == "w" && greenArray[3] == "o")
  {
    GreenMotorAClk();
    YellowMotorAClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  if (orangeArray[7] == "w" && yellowArray[7] == "o")
  {
    OrangeMotorClk();
    BlueMotorClk();
    YellowMotorClk();
    OrangeMotorAClk();
    OrangeMotorAClk();
  }
  //search white piece in blue face
  if (blueArray[1] == "w" && whiteArray[5] == "o")
  {
    BlueMotorClk();
    OrangeMotorClk();
  }
  if (blueArray[3] == "w" && redArray[5] == "o")
  {
    BlueMotorClk();
    BlueMotorClk();
    OrangeMotorClk();
  }
  if (blueArray[5] == "w" && orangeArray[3] == "o")
  {
    OrangeMotorClk();
  }
  if (blueArray[7] == "w" && yellowArray[5] == "o")
  {
    BlueMotorAClk();
    OrangeMotorClk();
  }
  //search white piece in green face
  if (greenArray[1] == "w" && whiteArray[3] == "o")
  {
    GreenMotorAClk();
    OrangeMotorAClk();
  }
  if (greenArray[3] == "w" && orangeArray[5] == "o")
  {
    OrangeMotorAClk();
  }
  if (greenArray[5] == "w" && redArray[3] == "o")
  {
    GreenMotorAClk();
    GreenMotorAClk();
    OrangeMotorAClk();
  }
  if (greenArray[7] == "w" && yellowArray[3] == "o")
  {
    GreenMotorClk();
    OrangeMotorAClk();
  }
  // for White Blue piece
  if (whiteArray[3] == "w" && greenArray[1] == "b")
  {
    GreenMotorAClk();
    GreenMotorAClk();
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  //search white piece in yellow face
  if (yellowArray[1] == "w" && redArray[7] == "b")
  {
    YellowMotorClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (yellowArray[7] == "w" && orangeArray[7] == "b")
  {
    YellowMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (yellowArray[5] == "w" && blueArray[7] == "b")
  {
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (yellowArray[3] == "w" && greenArray[7] == "b")
  {
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  //search white piece in red face

  if (redArray[3] == "w" && greenArray[5] == "b")
  {
    GreenMotorClk();
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (redArray[5] == "w" && blueArray[3] == "b")
  {
    BlueMotorClk();
  }
  if (redArray[7] == "w" && yellowArray[1] == "b")
  {
    RedMotorAClk();
    BlueMotorClk();
    RedMotorClk();
  }
  //search white piece in orange face

  if (orangeArray[3] == "w" && blueArray[5] == "b")
  {
    BlueMotorAClk();
  }
  if (orangeArray[5] == "w" && greenArray[3] == "b")
  {
    GreenMotorAClk();
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (orangeArray[7] == "w" && yellowArray[7] == "b")
  {
    OrangeMotorClk();
    BlueMotorAClk();
    OrangeMotorAClk();
  }
  //search white piece in blue face
  if (blueArray[1] == "w" && whiteArray[5] == "b")
  {
    BlueMotorAClk();
    RedMotorClk();
    YellowMotorClk();
    RedMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (blueArray[3] == "w" && redArray[5] == "b")
  {
    RedMotorClk();
    YellowMotorClk();
    RedMotorAClk();
    BlueMotorClk();
    BlueMotorClk();
  }
  if (blueArray[5] == "w" && orangeArray[3] == "b")
  {
    OrangeMotorAClk();
    YellowMotorAClk();
    OrangeMotorClk();
    BlueMotorClk();
    BlueMotorClk();
  }
  if (blueArray[7] == "w" && yellowArray[5] == "b")
  {
    YellowMotorClk();
    OrangeMotorClk();
    BlueMotorAClk();
    OrangeMotorAClk();
  }

  //search white piece in green face
  if (greenArray[1] == "w" && whiteArray[3] == "b")
  {
    GreenMotorAClk();
    OrangeMotorClk();
    YellowMotorAClk();
    OrangeMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (greenArray[3] == "w" && orangeArray[5] == "b")
  {
    OrangeMotorClk();
    YellowMotorAClk();
    OrangeMotorAClk();
    BlueMotorAClk();
    BlueMotorAClk();
  }
  if (greenArray[5] == "w" && redArray[3] == "b")
  {
    RedMotorAClk();
    YellowMotorClk();
    RedMotorClk();
    BlueMotorClk();
    BlueMotorClk();
  }
  if (greenArray[7] == "w" && yellowArray[3] == "b")
  {
    YellowMotorClk();
    OrangeMotorClk();
    BlueMotorAClk();
    OrangeMotorAClk();
  }
  // for White Green piece
  //search white piece in yellow face
  if (yellowArray[1] == "w" && redArray[7] == "g")
  {
    YellowMotorAClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (yellowArray[7] == "w" && orangeArray[7] == "g")
  {
    YellowMotorClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (yellowArray[5] == "w" && blueArray[7] == "g")
  {
    YellowMotorClk();
    YellowMotorClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (yellowArray[3] == "w" && greenArray[7] == "g")
  {
    GreenMotorAClk();
    GreenMotorAClk();
  }
  //search white piece in red face

  if (redArray[3] == "w" && greenArray[5] == "g")
  {
    GreenMotorAClk();
  }
  if (redArray[5] == "w" && blueArray[3] == "g")
  {
    BlueMotorAClk();
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (redArray[7] == "w" && yellowArray[1] == "g")
  {
    RedMotorClk();
    GreenMotorAClk();
    RedMotorAClk();
  }
  //search white piece in orange face

  if (orangeArray[3] == "w" && blueArray[5] == "g")
  {
    BlueMotorClk();
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorAClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (orangeArray[5] == "w" && greenArray[3] == "g")
  {
    GreenMotorClk();
  }
  if (orangeArray[7] == "w" && yellowArray[7] == "g")
  {
    OrangeMotorAClk();
    GreenMotorClk();
    OrangeMotorClk();
  }
  //search white piece in blue face
  if (blueArray[3] == "w" && redArray[5] == "g")
  {
    RedMotorClk();
    YellowMotorAClk();
    RedMotorAClk();
    GreenMotorClk();
    GreenMotorClk();
  }
  if (blueArray[5] == "w" && orangeArray[3] == "g")
  {
    OrangeMotorAClk();
    YellowMotorClk();
    OrangeMotorClk();
    GreenMotorClk();
    GreenMotorClk();
  }
  if (blueArray[7] == "w" && yellowArray[5] == "g")
  {
    YellowMotorClk();
    OrangeMotorAClk();
    GreenMotorAClk();
    OrangeMotorClk();
  }

  //search white piece in green face
  if (greenArray[1] == "w" && whiteArray[7] == "g")
  {
    GreenMotorAClk();
    OrangeMotorClk();
    YellowMotorClk();
    OrangeMotorAClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (greenArray[3] == "w" && orangeArray[5] == "g")
  {
    OrangeMotorClk();
    YellowMotorClk();
    OrangeMotorAClk();
    GreenMotorAClk();
    GreenMotorAClk();
  }
  if (greenArray[5] == "w" && redArray[3] == "g")
  {
    RedMotorAClk();
    YellowMotorAClk();
    RedMotorClk();
    GreenMotorClk();
    GreenMotorClk();
  }
  if (greenArray[7] == "w" && yellowArray[3] == "g")
  {
    YellowMotorAClk();
    OrangeMotorAClk();
    GreenMotorAClk();
    OrangeMotorClk();
  }
  // for White Corners
  // for red blue
  // middle layer
  if (redArray[0] == "w" && whiteArray[6] == "r" && greenArray[2] == "b")
  {
    RedMotorAClk();
    YellowMotorAClk();
    RedMotorClk();

  }
  if (redArray[2] == "w" && whiteArray[8] == "b" && blueArray[0] == "r")
  {
    RedMotorClk();
    YellowMotorClk();
    RedMotorAClk();
  }
  if (orangeArray[0] == "w" && whiteArray[2] == "r" && blueArray[2] == "b")
  {
    OrangeMotorAClk();
    YellowMotorAClk();
    OrangeMotorClk();

  }
  if (orangeArray[2] == "w" && whiteArray[0] == "b" && greenArray[0] == "r")
  {
    OrangeMotorClk();
    YellowMotorClk();
    OrangeMotorAClk();

  }
  if (blueArray[0] == "w" && whiteArray[8] == "r" && redArray[2] == "b")
  {
    BlueMotorAClk();
    YellowMotorAClk();
    BlueMotorClk();

  }
  if (blueArray[2] == "w" && whiteArray[6] == "b" && orangeArray[0] == "r")
  {
    BlueMotorClk();
    YellowMotorClk();
    BlueMotorAClk();
  }
  if (greenArray[0] == "w" && whiteArray[0] == "r" && blueArray[2] == "b")
  {
    GreenMotorAClk();
    YellowMotorAClk();
    GreenMotorClk();

  }
  if (greenArray[2] == "w" && whiteArray[6] == "b" && greenArray[0] == "r")
  {
    GreenMotorClk();
    YellowMotorClk();
    GreenMotorAClk();
  }
  //top and bottom layer
  if (whiteArray[0] == "w" && orangeArray[2] == "r" && greenArray[0] == "b")
  {
OrangeMotorClk();
YellowMotorClk();
OrangeMotorAClk();

  }
  if (whiteArray[2] == "w" && blueArray[2] == "r" && orangeArray[0] == "b")
  {
OrangeMotorAClk();
YellowMotorAClk();
OrangeMotorClk();
  }
  if (whiteArray[6] == "w" && redArray[2] == "r" && blueArray[0] == "b")
  {
RedMotorAClk();
YellowMotorAClk();
RedMotorClk();

  }
  if (whiteArray[8] == "w" && greenArray[2] == "r" && redArray[0] == "b")
  {
RedMotorClk();
YellowMotorClk();
RedMotorAClk();
  }
  if (yellowArray[0] == "w" && redArray[6] == "r" && greenArray[8] == "b")
  {
RedMotorAClk();
YellowMotorClk();
RedMotorClk();

  }
  if (yellowArray[2] == "w" && blueArray[6] == "r" && redArray[8] == "b")
  {
RedMotorClk();
YellowMotorAClk();
RedMotorAClk();

  }
  if (yellowArray[8] == "w" && orangeArray[6] == "r" && blueArray[8] == "b")
  {
OrangeMotorClk();
YellowMotorAClk();
OrangeMotorAClk();

  }
  if (yellowArray[6] == "w" && greenArray[6] == "r" && orangeArray[8] == "b")
  {
OrangeMotorAClk();
YellowMotorClk();
OrangeMotorClk();

  }
  //final touch
  if (redArray[6] == "w" && yellowArray[0] == "b" && greenArray[8] == "r")
  {
    YellowMotorClk();
    YellowMotorClk();
    RedMotorClk();
    YellowMotorAClk();
    RedMotorAClk();
  }
  if (redArray[8] == "w" && yellowArray[2] == "r" && blueArray[6] == "b")
  {
    YellowMotorAClk();
    BlueMotorClk();
    YellowMotorClk();
    BlueMotorAClk();

  }
  if (orangeArray[6] == "w" && yellowArray[8] == "b" && blueArray[8] == "r")
  {
    RedMotorClk();
    YellowMotorAClk();
    RedMotorAClk();

  }
  if (orangeArray[8] == "w" && yellowArray[6] == "r" && greenArray[6] == "b")
  {
    YellowMotorClk();
    BlueMotorAClk();
    YellowMotorClk();
    BlueMotorClk();

  }
  if (blueArray[6] == "w" && yellowArray[2] == "b" && redArray[8] == "r")
  {
    YellowMotorClk();
    RedMotorClk();
    YellowMotorAClk();
    RedMotorAClk();

  }
  if (blueArray[8] == "w" && yellowArray[8] == "r" && orangeArray[6] == "b")
  {
    YellowMotorAClk();
    YellowMotorAClk();
    BlueMotorAClk();
    YellowMotorClk();
    BlueMotorClk();

  }
  if (greenArray[6] == "w" && yellowArray[6] == "b" && orangeArray[8] == "r")
  {
    YellowMotorAClk();
    RedMotorClk();
    YellowMotorAClk();
    RedMotorAClk();

  }
  if (greenArray[8] == "w" && yellowArray[0] == "r" && redArray[6] == "b")
  {
    BlueMotorAClk();
    YellowMotorClk();
    BlueMotorClk();

  }


  // for blue orange

  // for orange green
  // for green red




}// around 400 if statements
void loop()
{
  /* for (int i = 0; i < 9; i++)
     if (newwhiteArray[i] != "")
       whiteArray[i] = newwhiteArray[i];
    for (int i = 0; i < 9; i++)
     if (newyellowArray[i] != "")
       yellowArray[i] = newyellowArray[i];
    for (int i = 0; i < 9; i++)
     if (newredArray[i] != "")
       redArray[i] = newredArray[i];
    for (int i = 0; i < 9; i++)
     if (neworangeArray[i] != "")
       orangeArray[i] = neworangeArray[i];
    for (int i = 0; i < 9; i++)
     if (newblueArray[i] != "")
       blueArray[i] = newblueArray[i];
    for (int i = 0; i < 9; i++)
     if (newgreenArray[i] != "")
       greenArray[i] = newgreenArray[i];*/
}
