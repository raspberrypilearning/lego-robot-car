## Управляй своими моторами с помощью приложения Blue Dot

Приложение Blue Dot и библиотеку Python можно использовать для управления моторами LEGO® Technic™ с твоего устройства.

--- task ---

Снова откройте файл `bt_car.py` и пропиши Blue Dot в верхней части файла. Ты также должен заменить импорт `sleep` на `from signal import pause`.

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

motor_left = Motor('A')     
motor_right = Motor('B')     
dot = BlueDot() 

--- /task ---

--- task ---

Удали цикл `for` из твоего текущего кода, чтобы полный код выглядел так:

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

motor_left = Motor('A')     
motor_right = Motor('B')     
dot = BlueDot()     


def stop():     
    motor_left.stop()     
    motor_right.stop()     


def forward():     
    motor_left.start(-100)     
    motor_right.start(100)     


def backward():     
    motor_left.start(100)     
    motor_right.start(-100)     


def right():     
    motor_left.start(-100)     
    motor_right.start(-100)     


def left():     
    motor_left.start(100)     
    motor_right.start(100)     
--- /code ---

--- /task ---

--- task ---

Теперь добавь функцию, которая использует Blue Dot для **вызова** функции `forward` в конец твоего скрипта.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 34
line_highlights: 
---

def move(pos):     
    if pos.top:     
        forward()  

--- /code ---

--- /task ---

Функция `move` имеет единственный параметр, который называется `pos`. Он будет автоматически передан функции, в зависимости от того, где коснулись внутри Blue Dot.

--- task ---

Добавь вызовы двух методов в конец твоего кода. Они заставят автомобиль двигаться вперед и останавливаться. Последний вызов гарантирует, что программа не просто закончится в нижней части скрипта.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 39
line_highlights: 
---

dot.when_pressed = move    
dot.when_released = stop   
pause() 

--- /code ---

--- /task ---

--- task ---

Запусти свой код. В приложении Blue Dot на твоем устройстве нажми синюю точку вверху, и моторы должны включиться. Когда ты уберешь палец с синей точки, моторы должны остановиться.

--- /task ---

На данный момент моторы будут крутить колеса только вперед. Используя параметр `pos`, ты можешь заставить их вращаться во всех направлениях.

--- task ---

Добавь к твоей функции `move` этот код, чтобы моторы двигали машину назад, влево и вправо.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 32
line_highlights: 37-42
---


def move(pos):    
    if pos.top:    
        forward()    
    elif pos.bottom:    
        backward()    
    elif pos.left:    
        left()     
    elif pos.right:    
        right()     


--- /code ---

--- /task ---

--- task ---

Запусти свой код еще раз и протестируй его с помощью приложения Blue Dot. Нажатие на правую, левую и нижнюю часть синей точки теперь должно вращать моторы в разные направления.

--- /task ---

Вы можешь добавить в свой код одну строчку, чтобы Blue Dot реагировал не только на нажатия, но и на перемещение пальца по синей точке.

--- task ---

Добавьте эту единственную строчку, чтобы моторы реагировали на движение пальца над синей точкой.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 43
line_highlights: 47
---


dot.when_pressed = move    
dot.when_released = stop    
dot.when_moved = move  
   
--- /code ---

--- /task ---

--- task ---

Запусти свою программу и поэкспериментируй, нажимая синюю точку на устройстве Android и перемещая палец в разные положения. Моторы должны вращаться в разных направлениях и останавливаться, когда ты убираешь палец с синей точки.

--- /task ---

Чтобы прочитать полную документацию по BlueDot, [нажми здесь](https://bluedot.readthedocs.io/ru-RU/latest/).

--- save ---
