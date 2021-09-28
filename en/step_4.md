## Control your motors with Blue Dot

The Blue Dot app and Python library can be used to control your motors, from your device.

--- task ---

Open up the `bt_car.py` file again, and set up Blue Dot at the top of the file. You can also remove the `sleep` import.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 
line_highlights: 3,7
---
from buildhat import Motor    
from bluedot import BlueDot    

motor_left = Motor('A')     
motor_right = Motor('B')     
bd = BlueDot()     
--- /code ---

--- /task ---

--- task ---

Remove the `for` loop from your current code, so that the complete code looks like this:

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 
line_highlights: 
---
from buildhat import Motor    
from bluedot import BlueDot     

motor_left = Motor('A')     
motor_right = Motor('B')     
bd = BlueDot()     


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

Now add a function that uses Blue Dot to **call** the the `forward` function.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 32
line_highlights: 
---


def move(pos):     
    if pos.top:     
        forward()     
--- /code ---

--- /task ---

The `move` function has a single parameter, which has been called `pos`. This will be automatically passed to the function, depending on where the Blue Dot is touched.

--- task ---

Add two method calls to your code. These will make the car move forward and stop.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 37
line_highlights: 
---


bd.when_pressed = move    
bd.when_released = stop    
--- /code ---

--- /task ---

--- task ---

Run your code. On the Blue Dot app on your device, press the blue dot near the top and the motors should turn. When you take your finger off the blue dot, the motors should stop.

--- /task ---

At the moment, the motors will only turn the wheels in the forward direction. By using the `pos` parameter, you can make them turn in all directions.

--- task ---

Add to your `move` function so that the motors can turn the wheels backwards, left, and right.

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

Run your code again, and test it with the Blue Dot app. Pressing on the right, left, and bottom of the blue dot should now move the motors in different directions.

--- /task ---

You can add a single line to your code, so that Blue Dot responds not only to presses, but also to when your finger moves over the blue dot.

--- task ---

Add this single line so that the motors respond to motion over the blue dot.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 43
line_highlights: 47
---


bd.when_pressed = move    
bd.when_released = stop    
bd.when_moved = move     
--- /code ---

--- /task ---

--- task ---

Run your program and experiment with pressing the blue dot on your Android device, and moving your finger around to different positions. The motors should spin in different directions, and stop when you lift your finger off the blue dot.

--- /task ---

--- save ---
