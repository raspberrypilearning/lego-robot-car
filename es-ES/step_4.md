## Controla tus motores con Blue Dot

La aplicación y la biblioteca Python Blue Dot se pueden usar para controlar tus motores LEGO® Technic ™ desde tu dispositivo.

--- task ---

Abra el archivo `bt_car.py` nuevamente y configura Blue Dot en la parte superior del archivo. También debes reemplazar la importación `sleep` con `from signal import pause`.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 1
line_highlights: 2,3,7
---

from buildhat import Motor    
from bluedot import BlueDot 
from signal import pause

motor_izquierda = Motor('A')     
motor_dercha = Motor('B')     
punto = BlueDot()

--- /code ---

--- /task ---

--- task ---

Elimina el bucle `for` de tu código actual, de modo que el programa completo se vea así:

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 1
line_highlights:
---

from buildhat import Motor    
from bluedot import BlueDot     
from signal import pause

motor_izquierda = Motor('A')     
motor_dercha = Motor('B')     
punto = BlueDot()


def detener():     
    motor_izuierda.stop()     
    motor_derecha.stop()


def avanzar():     
    motor_izquierda.start(-100)     
    motor_derecha.start(100)


def atras():     
    motor_izquierda.start(100)     
    motor_derecha.start(-100)


def derecha():     
    motor_izquierda.start(-100)     
    motor_derecha.start(-100)


def izquierda():     
    motor_izquierda.start(100)     
    motor_derecha.start(100)     
--- /code ---

--- /task ---

--- task ---

Ahora agrega una función que use Blue Dot para **llamar** la función `avanzar` al final de tu secuencia de comandos.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 34
line_highlights:
---

def mover(pos):     
    if pos.top:     
        avanzar()

--- /code ---

--- /task ---

La función `mover` tiene un solo parámetro, que se llama `pos`. Éste se pasará automáticamente a la función, dependiendo de dónde se toque el punto azul.

--- task ---

Agrega dos llamadas a métodos al final de tu programa. Esto hará que el automóvil avance y se detenga. La llamada final se asegura de que el programa no termine al final del programa.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 39
line_highlights:
---

punto.when_pressed = mover    
punto.when_released = detener   
pause()

--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa. En la aplicación Blue Dot de tu dispositivo, presiona el punto azul cerca de la parte superior y los motores deberían girar. Cuando quitas el dedo del punto azul, los motores deben detenerse.

--- /task ---

Por el momento, los motores solo harán girar las ruedas hacia adelante. Usando el parámetro `pos`, puedes hacer que giren en todas las direcciones.

--- task ---

Agrega a tu función `mover` para que los motores muevan el carro hacia atrás, hacia la izquierda y hacia la derecha.

--- code ---
---
language: python 
filename: bt_car.py 
line_numbers: true 
line_number_start: 32
line_highlights: 37-42
---


def mover(pos):    
    if pos.top:    
        avanzar()    
    elif pos.bottom:    
        atras()    
    elif pos.left:    
        izquierda()     
    elif pos.right:    
        derecha()


--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa nuevamente y pruébalo con la aplicación Blue Dot. Al presionar en la derecha, en la izquierda y en la parte inferior del punto azul, los motores ahora se deben mover en diferentes direcciones.

--- /task ---

Puedes agregar una sola línea a ru código, de modo que Blue Dot responda no solo a las presiones, sino también cuando tu dedo se mueve sobre el punto azul.

--- task ---

Agrega esta línea para que los motores respondan al movimiento sobre el punto azul.

--- code ---
---
language: python 
filename: 
line_numbers: true 
line_number_start: 43
line_highlights: 47
---


punto.when_pressed = mover    
punto.when_released = detener    
punto.when_moved = mover

--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa y experimenta presionando el punto azul en tu dispositivo Android y moviendo el dedo a diferentes posiciones. Los motores deben girar en diferentes direcciones y detenerse cuando levantas el dedo del punto azul.

--- /task ---

Para leer la documentación completa de BlueDot, [haz clic aquí](https://bluedot.readthedocs.io/es-ES/latest/).

--- save ---
