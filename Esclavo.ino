#include <Wire.h>


void setup() {
  
  for (int i = 2; i < 12; i++) {
    pinMode(i, OUTPUT); // Configurar los pines de los LEDs como salida
    digitalWrite(i, LOW); // Apagar todos los LEDs al principio
  }
  
  Wire.begin(1); // Inicializar la comunicación I2C como esclavo con dirección 1
  Wire.onReceive(receiveEvent); // Configurar la función de callback para manejar los datos recibidos
  Serial.begin(9600); // Inicializar el monitor serial
  
}

void loop() {
  delay(100); 
}

// Función para manejar los datos recibidos
void receiveEvent(int howMany) { 
  String receivedData = "";
  while (Wire.available()) { // Leer todos los bytes disponibles
    char c = Wire.read(); // Leer el byte actual
    receivedData += c; // Concatenar el byte al string recibido
  }
  
  // Enviar los datos recibidos por 
  // el puerto serial al Python
  Serial.write(receivedData.c_str());
  
  // Encender los LEDs según los datos recibidos
  for (int i = 0; i < 10; i++) {
    if (receivedData.charAt(i) == '1') {
      digitalWrite(2 + i, HIGH); 
    } else {
      digitalWrite(2 + i, LOW); 
    }
  }
 
}