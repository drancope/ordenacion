``` C++
#include <Servo.h> // Incluye la librería Servo [5]

Servo myservo;  // Crea el objeto servo para controlar [6]
int pos = 0;    // Variable para almacenar la posición [7]

void setup() {
  myservo.attach(9);  // Vincula el servo al pin 9 [6]
}

void loop() {
  // Va de 0 a 180 grados en pasos de 1 grado
  for (pos = 0; pos <= 180; pos += 1) { 
    myservo.write(pos);              // Dice al servo ir a la posición
    delay(15);                       // Espera 15ms para que llegue [1]
  }
  // Va de 180 a 0 grados
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);              // Dice al servo ir a la posición
    delay(15);                       // Espera 15ms para que llegue
  }
}
```
