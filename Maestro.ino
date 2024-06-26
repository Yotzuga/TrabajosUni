#include <Wire.h>

void setup() {
  Wire.begin();        // Inicializar la comunicación I2C como maestro
  Serial.begin(9600);  // Inicializar el monitor serial
  
  // Configurar los pines de los LEDs como salida y apagarlos al principio
  for (int i = 2; i < 12; i++) {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
  }
}

void loop() {
  if (Serial.available() > 0) { // Verificar si hay datos disponibles en el puerto serial
    String dataReceived = Serial.readString(); // Leer los datos recibidos del puerto serial
    Serial.println("Datos recibidos del Raspberry Pi: " + dataReceived); // Imprimir los datos recibidos
    
    // Encender los LEDs según los datos recibidos
    for (int i = 0; i < 10; i++) {
      if (dataReceived.charAt(i) == '1') {
        digitalWrite(2 + i, HIGH); // Encender el LED correspondiente si el dato es '1'
      } else {
        digitalWrite(2 + i, LOW); // Apagar el LED correspondiente si el dato es '0'
      }
    }

    // Enviar los datos al Arduino esclavo con la dirección 1
    Wire.beginTransmission(1);   // Dirección del esclavo
    Wire.write(dataReceived.c_str(), dataReceived.length()); // Enviar los datos recibidos
    Wire.endTransmission();     // Finalizar la transmisión
  }
  
  
  
  delay(100); // Esperar un momento antes de revisar nuevamente
}