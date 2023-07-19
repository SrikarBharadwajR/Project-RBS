String whiteArray[9] =  {"y", "b", "g", "r", "w", "o", "w", "g", "w"};
String yellowArray[9] = {"r", "y", "g", "b", "y", "w", "o", "b", "g"};
String redArray[9] =    {"o", "w", "r", "y", "r", "y", "g", "g", "w"};
String orangeArray[9] = {"y", "o", "b", "g", "o", "w", "w", "r", "y"};
String blueArray[9] =   {"b", "r", "o", "r", "b", "r", "r", "o", "o"};
String greenArray[9] =  {"r", "w", "b", "b", "g", "o", "b", "y", "y"};

void WhiteMotorClk()
{
  digitalWrite(1, HIGH);
  delay(1000);
  digitalWrite(1, LOW);
  redArray[0] = blueArray[0];
  redArray[1] = blueArray[1];
  redArray[2] = blueArray[2];
  blueArray[0] = orangeArray[0];
  blueArray[1] = orangeArray[1];
  blueArray[2] = orangeArray[2];
  orangeArray[0] = greenArray[0];
  orangeArray[1] = greenArray[1];
  orangeArray[2] = greenArray[2];
  greenArray[0] = redArray[0];
  greenArray[1] = redArray[1];
  greenArray[2] = redArray[2];
  Serial.println("White Motor Turned ClockWise");
}
void WhiteMotorAClk()
{
  digitalWrite(7, HIGH);
  delay(1000);
  digitalWrite(7, LOW);
  blueArray[0] = redArray[0];
  blueArray[1] = redArray[1];
  blueArray[2] = redArray[2];
  redArray[0] = greenArray[0];
  redArray[1] = greenArray[1];
  redArray[2] = greenArray[2];
  greenArray[0] = orangeArray[0];
  greenArray[1] = orangeArray[1];
  greenArray[2] = orangeArray[2];
  orangeArray[0] = blueArray[0];
  orangeArray[1] = blueArray[1];
  orangeArray[2] = blueArray[2];
  Serial.println("White Motor Turned Anti ClockWise");
}
void YellowMotorClk()
{
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);
  blueArray[6] = redArray[6];
  blueArray[7] = redArray[7];
  blueArray[8] = redArray[8];
  redArray[6] = greenArray[6];
  redArray[7] = greenArray[7];
  redArray[8] = greenArray[8];
  greenArray[6] = orangeArray[6];
  greenArray[7] = orangeArray[7];
  greenArray[8] = orangeArray[8];
  orangeArray[6] = blueArray[6];
  orangeArray[7] = blueArray[7];
  orangeArray[8] = blueArray[8];
  Serial.println("Yellow Motor Turned ClockWise");
}
void YellowMotorAClk()
{
  digitalWrite(8, HIGH);
  delay(1000);
  digitalWrite(8, LOW);
  redArray[6] = blueArray[6];
  redArray[7] = blueArray[7];
  redArray[8] = blueArray[8];
  blueArray[6] = orangeArray[6];
  blueArray[7] = orangeArray[7];
  blueArray[8] = orangeArray[8];
  orangeArray[6] = greenArray[6];
  orangeArray[7] = greenArray[7];
  orangeArray[8] = greenArray[8];
  greenArray[6] = redArray[6];
  greenArray[7] = redArray[7];
  greenArray[8] = redArray[8];
  Serial.println("Yellow Motor Turned Anti ClockWise");
}
void RedMotorClk()
{
  digitalWrite(3, HIGH);
  delay(1000);
  digitalWrite(3, LOW);
  String newblueArray[9];
  newblueArray[0] = whiteArray[6];
  newblueArray[3] = whiteArray[7];
  newblueArray[6] = whiteArray[8];
  yellowArray[2] = blueArray[0];
  yellowArray[1] = blueArray[3];
  yellowArray[0] = blueArray[6];
  greenArray[2] = yellowArray[0];
  greenArray[5] = yellowArray[1];
  greenArray[8] = yellowArray[2];
  whiteArray[8] = greenArray[2];
  whiteArray[7] = greenArray[5];
  whiteArray[6] = greenArray[8];
  for (int i = 0; i < 9; i++)
    blueArray[i] = newblueArray[i];
  Serial.println("Red Motor Turned ClockWise");
}
void RedMotorAClk()
{
  digitalWrite(9, HIGH);
  delay(1000);
  digitalWrite(9, LOW);
  whiteArray[6] = blueArray[0];
  whiteArray[7] = blueArray[3];
  whiteArray[8] = blueArray[6];
  blueArray[0] = yellowArray[2];
  blueArray[3] = yellowArray[1];
  blueArray[6] = yellowArray[0];
  yellowArray[0] = greenArray[2];
  yellowArray[1] = greenArray[5];
  yellowArray[2] = greenArray[8];
  greenArray[2] = whiteArray[8];
  greenArray[5] = whiteArray[7];
  greenArray[8] = whiteArray[6];
  Serial.println("Red Motor Turned Anti ClockWise");
}
void OrangeMotorClk()
{
  digitalWrite(4, HIGH);
  delay(1000);
  digitalWrite(4, LOW);
  whiteArray[0] = blueArray[2];
  whiteArray[1] = blueArray[5];
  whiteArray[2] = blueArray[8];
  blueArray[8] = yellowArray[6];
  blueArray[5] = yellowArray[7];
  blueArray[2] = yellowArray[8];
  yellowArray[6] = greenArray[0];
  yellowArray[7] = greenArray[3];
  yellowArray[8] = greenArray[6];
  greenArray[0] = whiteArray[2];
  greenArray[3] = whiteArray[1];
  greenArray[6] = whiteArray[0];
  Serial.println("Orange Motor Turned ClockWise");
}
void OrangeMotorAClk()
{
  digitalWrite(10, HIGH);
  delay(1000);
  digitalWrite(10, LOW);
  blueArray[2] = whiteArray[0];
  blueArray[5] = whiteArray[1];
  blueArray[8] = whiteArray[2];
  yellowArray[6] = blueArray[8];
  yellowArray[7] = blueArray[5];
  yellowArray[8] = blueArray[2];
  greenArray[0] = yellowArray[6];
  greenArray[3] = yellowArray[7];
  greenArray[6] = yellowArray[8];
  whiteArray[2] = greenArray[0];
  whiteArray[1] = greenArray[3];
  whiteArray[0] = greenArray[6];
  Serial.println("Orange Motor Turned Anti ClockWise");
}
void BlueMotorClk()
{
  digitalWrite(5, HIGH);
  delay(1000);
  digitalWrite(5, LOW);
  redArray[0] = blueArray[0];
  redArray[1] = blueArray[1];
  redArray[2] = blueArray[2];
  blueArray[0] = orangeArray[0];
  blueArray[1] = orangeArray[1];
  blueArray[2] = orangeArray[2];
  orangeArray[0] = greenArray[0];
  orangeArray[1] = greenArray[1];
  orangeArray[2] = greenArray[2];
  greenArray[0] = redArray[0];
  greenArray[1] = redArray[1];
  greenArray[2] = redArray[2];
  Serial.println("Blue Motor Turned ClockWise");
}
void BlueMotorAClk()
{
  digitalWrite(11, HIGH);
  delay(1000);
  digitalWrite(11, LOW);
  blueArray[0] = redArray[0];
  blueArray[1] = redArray[1];
  blueArray[2] = redArray[2];
  redArray[0] = greenArray[0];
  redArray[1] = greenArray[1];
  redArray[2] = greenArray[2];
  greenArray[0] = orangeArray[0];
  greenArray[1] = orangeArray[1];
  greenArray[2] = orangeArray[2];
  orangeArray[0] = blueArray[0];
  orangeArray[1] = blueArray[1];
  orangeArray[2] = blueArray[2];
  Serial.println("Blue Motor Turned Anti ClockWise");
}
void GreenMotorClk()
{
  digitalWrite(6, HIGH);
  delay(1000);
  digitalWrite(6, LOW);
  redArray[0] = blueArray[0];
  redArray[1] = blueArray[1];
  redArray[2] = blueArray[2];
  blueArray[0] = orangeArray[0];
  blueArray[1] = orangeArray[1];
  blueArray[2] = orangeArray[2];
  orangeArray[0] = greenArray[0];
  orangeArray[1] = greenArray[1];
  orangeArray[2] = greenArray[2];
  greenArray[0] = redArray[0];
  greenArray[1] = redArray[1];
  greenArray[2] = redArray[2];
  Serial.println("Green Motor Turned ClockWise");
}
void GreenMotorAClk()
{
  digitalWrite(12, HIGH);
  delay(1000);
  digitalWrite(12, LOW);
  blueArray[0] = redArray[0];
  blueArray[1] = redArray[1];
  blueArray[2] = redArray[2];
  redArray[0] = greenArray[0];
  redArray[1] = greenArray[1];
  redArray[2] = greenArray[2];
  greenArray[0] = orangeArray[0];
  greenArray[1] = orangeArray[1];
  greenArray[2] = orangeArray[2];
  orangeArray[0] = blueArray[0];
  orangeArray[1] = blueArray[1];
  orangeArray[2] = blueArray[2];
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
  pinMode(7, OUTPUT);//WhiteAClk
  pinMode(8, OUTPUT);//Yellow
  pinMode(9, OUTPUT);//Red should always be in top for Y and facing towards you while measuring white
  pinMode(10, OUTPUT);//Orange
  pinMode(11, OUTPUT);//Blue
  pinMode(12, OUTPUT);//Green
  WhiteMotorClk();
}
void loop()
{
}
