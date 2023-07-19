String blueArray[9] =   {"b", "r", "o", "r", "b", "r", "r", "o", "o"};
void test()
{
  String newblueArray[9];
  newblueArray[0] = "6";
  newblueArray[3] = "7";
  newblueArray[6] = "8";
  for (int i = 0; i < 9; i++)
  {
    blueArray[i] = newblueArray[i];
    Serial.println(blueArray[i]); 
  }
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  test();
}

void loop() {
  // put your main code here, to run repeatedly:

}
