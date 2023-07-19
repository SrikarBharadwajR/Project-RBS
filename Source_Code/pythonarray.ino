int datafromUser=0;
void setup() {
  
  pinMode( 5, OUTPUT );
  pinMode( 6, OUTPUT );
  pinMode( 7, OUTPUT );
  pinMode( 8, OUTPUT );
  pinMode( 9, OUTPUT );
  pinMode( 10, OUTPUT );
  Serial.begin(9600);
}

void   loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
    Serial.println(datafromUser);
  }

  if(datafromUser ==  '1'){
    digitalWrite( 5, HIGH); 
  }
  if(datafromUser  == '2'){ 
    digitalWrite( 6, HIGH);
  }
  if(datafromUser  == '3'){ 
    digitalWrite( 7, HIGH);
  }
  if(datafromUser == '4'){
    digitalWrite( 8, HIGH); 
  }
  if(datafromUser  == '5'){ 
    digitalWrite( 9, HIGH);
  }
  if(datafromUser  == '6'){ 
    digitalWrite( 10, HIGH);
  }
  
}
