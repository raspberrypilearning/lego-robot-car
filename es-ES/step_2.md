## Configuración de los motores LEGO® Spike ™

Es más fácil probar y desarrollar tu programa antes de construir tu robot. Esto reduce el riesgo de arruinar tu maravilloso modelo cuando un motor envía inesperadamente al robot en la dirección incorrecta y se sale de tu escritorio (aunque, por supuesto, lo bueno de usar LEGO® es que siempre puedes reconstruir).

El build HAT de Raspberry Pi y su biblioteca Python te permiten controlar los motores LEGO® Technic ™ directamente desde tu ordenador Raspberry Pi.

Enchufa dos motores en los puertos A y B del Build HAT de la Raspberry Pi. Conecta tus baterías al conector de barril del Build HAT y enciéndelo.

### Haz girar los motores

--- task ---

Abre Thonny en tu Raspberry Pi desde el menú **Programación**.

--- /task ---

--- task ---

Utiliza el siguiente código para hacer girar ambos motores al 50% de su velocidad máxima durante 10 segundos. (Van a girar uno a la vez, no juntos)

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start:
line_highlights:
---

from buildhat import Motor   
from time import sleep

motor_izquierda = Motor('A')   
motor_derecha = Motor('B')   
motor_izquierda.run_for_seconds(seconds=10, speed=50)   
motor_derecha.run_for_seconds(seconds=10, speed=-50)

--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa y comprueba que los motores giran.

--- /task ---

Tu programa actual debe mover los motores en direcciones opuestas, porque los motores se montarán en lados opuestos del chasis del automóvil. Por lo tanto, la rotación en sentido antihorario en la rueda de la izquierda moverá el robot hacia adelante, mientras que se necesita una rotación en horaria en el lado derecho.

Ahora que has probado los motores, puedes crear funciones para hacer que los motores se detengan y avancen.

--- task ---

Elimina las dos líneas de código que hacen que los motores funcionen durante 10 segundos y agrega estas dos funciones. La función `empezar()` funciona de manera diferente a las funciones `run` de los motores LEGO, por lo que esta vez funcionarán juntas.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start:
line_highlights: 7-14
---

from buildhat import Motor   
from time import sleep

motor_izquierda = Motor('A')    
motor_derecha = Motor('B')

def detener():    
    motor_izuierda.stop()    
    motor_derecha.stop()


def avanzar():     
    motor_izquierda.start(50)     
    motor_derecha.start(-50)


--- /code ---

--- /task ---

--- task ---

Prueba tus funciones agregando la siguiente secuencia de inicio-parada-inicio-parada:

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 17
line_highlights:
---

for i in range(2):    
    avanzar()    
    sleep(1)    
    detener()    
    sleep(1)

--- /code ---
--- /task ---


Una vez que funcione, agrega tres funciones más para mover el robot hacia atrás, hacia la izquierda y hacia la derecha.

--- task ---

Para mover el robot hacia atrás, simplemente invierta las direcciones de ambos motores.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 17
line_highlights:
---

def atras():    
    motor_izquierda.start(-50)     
    motor_derecha.start(50)


--- /code ---

--- /task ---

--- task ---

Para girar el robot hacia la izquierda, ambos motores deben girar en la misma dirección.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 22
line_highlights:
---

def izquierda(): 
    motor_izquierda.start(50) 
    motor_derecha.start(50)


def derecha(): 
    motor_izquierda.start(-50) 
    motor_derecha.start(-50)


--- /code ---

--- /task ---

--- task ---

Para probar tu código, puedes editar su bucle `for`.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 32
line_highlights:
---

for i in range(2):    
    avanzar()     
    sleep(1)     
    atras()     
    sleep(1)     
    derecha()     
    sleep(1)     
    izquierda()      
    sleep(1)      
    detener()

--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa y comprueba que las ruedas giran correctamente.

--- /task ---

--- save ---
