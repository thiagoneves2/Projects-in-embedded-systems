#include <Wire.h>

// Define o pino do potenciômetro
int potPin = A0;


//Função que realiza a medida e envia para a Rasp
void request_d()
{
  //Faz a medida do potenciometro
  int potV = analogRead(potPin);

  //Manda 2 bytes de informação, dividindo a informação para que possa ser lida pela Rasp
  Wire.write(highByte(potV));
  Wire.write(lowByte(potV));

  //Print no monitor serial do arduino o valor do potenciometro
  Serial.println(potV);
}

void setup() {

  //Configura o monitor
  Serial.begin(9600);

  //Configura a função Wire para o endereço 8
  Wire.begin(0x8);

  //Quando houver requisição de informação chama a função request_d
  Wire.onRequest(request_d);
}

void loop() { 
  delay(100);
}

