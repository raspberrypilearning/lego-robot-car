## Настройка моторов LEGO® Spike™

Перед сборкой робота проще протестировать и разработать твою программу. Это снижает риск испортить твою замечательную модель, когда мотор неожиданно отправляет робота в неправильном направлении, и он падает с твоего стола (хотя, конечно, преимущество использования LEGO® в том, что ты всегда можешь все переделать).

Плата Raspberry Pi Build HAT и библиотека Python для неё позволяют тебе управлять двигателями LEGO® Technic™ прямо с твоего компьютера Raspberry Pi.

Подключи два двигателя к портам A и B на плате Raspberry Pi Build HAT. Подключи свой батарейный отсек к циллиндрическому разъему на плате Build HAT и включи его.

### Заставь моторы вращаться

--- task ---

Открой Thonny на твоем Raspberry Pi из меню **Программирование**.

--- /task ---

--- task ---

Используй следующий код, чтобы вращать оба двигателя на 50% от их максимальной скорости в течение 10 секунд. (Они будут работать по одному, а не вместе.)

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

motor_left = Motor('A')   
motor_right = Motor('B')   
motor_left.run_for_seconds(seconds=10, speed=50)   
motor_right.run_for_seconds(seconds=10, speed=-50)    

--- /code ---

--- /task ---

--- task ---

Запусти твою программу и проверь, как вращаются моторы.

--- /task ---

Твоя текущая программа должна перемещать двигатели в противоположных направлениях, потому что двигатели будут установлены на противоположных сторонах шасси автомобиля. Таким образом, вращение левого колеса против часовой стрелки будет перемещать робота вперед, тогда как для правого колеса требуется вращение по часовой стрелке.

Теперь, когда ты проверил двигатели, ты можешь создавать такие функции, чтобы двигатели останавливались и двигались вперед.

--- task ---

Удали две строки кода, которые заставляют двигатели работать в течение 10 секунд, и добавь эти две функции. Функция `start()` работает иначе, чем функции LEGO двигателей `run`, поэтому на этот раз они будут работать вместе.

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

motor_left = Motor('A')    
motor_right = Motor('B')    

def stop():    
  motor_left.stop()    
  motor_right.stop()    


def forward():     
  motor_left.start(50)     
  motor_right.start(-50)     


--- /code ---

--- /task ---

--- task ---

Проверь свои функции, добавив следующую последовательность старт-стоп-старт-стоп:

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 17
line_highlights: 
---

for i in range(2):    
  forward()    
  sleep(1)    
  stop()    
  sleep(1)  

--- /code ---
--- /task ---


Как только это заработает, добавь еще три функции для перемещения робота назад, влево и вправо.

--- task ---

Чтобы переместить робота назад, просто поменяй направление вращения обоих двигателей на противоположное.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 17
line_highlights: 
---

def back():    
  motor_left.start(-50)     
  motor_right.start(50)      


--- /code ---

--- /task ---

--- task ---

Чтобы повернуть робота влево, оба мотора должны вращаться в одном направлении.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 22
line_highlights: 
---

def left():
  motor_left.start(50)
  motor_right.start(50)


def right():
  motor_left.start(-50)
  motor_right.start(-50)


--- /code ---

--- /task ---

--- task ---

Чтобы проверить свой код, ты можешь отредактировать цикл `for`.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 32
line_highlights: 
---

for i in range(2):    
  forward()     
  sleep(1)     
  back()     
  sleep(1)     
  right()     
  sleep(1)     
  left()      
  sleep(1)      
  stop()    
    
--- /code ---

--- /task ---

--- task ---

Запусти свой код и убедись, что колеса вращаются правильно.

--- /task ---

--- save ---
