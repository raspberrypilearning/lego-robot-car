## Setting up the Motors

It is easier to test and develop your program before building your robot. This reduces the risk of ruining your wonderful model when a motor unexpectedly sends the robot in the wrong direction and it careens off your desk (although, of course, the good thing about using LEGO is that you always rebuild).

The Raspberry Pi Build HAT and its Python library allow you to control LEGO Technic motors directly from your Raspberry Pi computer.

Plug two motors into ports A and B on the Raspberry Pi Build HAT.  Connect your battery pack to the barrel jack on the Build HAT and turn it on. 

### Make the motors spin

--- task ---

Open Thonny on your Raspberry Pi from the Programming menu.

--- /task ---

--- task ---

Use the following code to spin both motors at 50% of their maximum speed for 10 seconds.

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
motor_left.run_for_seconds(10, 50)
motor_right.run_for_seconds(10, -50)
--- /code ---

--- /task ---

--- task ---

Run your program and check the motors turn.

--- /task ---

Your current program should move the motors in opposite directions, because the motors will be mounted on opposite sides of the car's chassis. So anti-clockwise rotation on the left hand wheel will move the robot forward, whereas a clockwise rotation is needed on the right hand side.

Now that you have tested the motors, you can create functions to make the motors stop and drive forward.

--- task ---

Remove the two lines of code that make the motors run for 10 seconds, and add these two functions.

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

Test your functions out by adding the following start-stop-start-stop sequence:

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


Once that works, add 3 more functions to move the robot backwards, left and right.

--- task ---

To move the robot backwards, simply reverse the directions of both motors.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 17
line_highlights: 
---
def back():
  motor_l.start(-50)
  motor_r.start(50)


--- /code ---

--- /task ---

--- task ---

To turn the robot to the left, both motors need to turn in the same direction.

--- code ---
---
language: python
filename: bt_car.py
line_numbers: true
line_number_start: 22
line_highlights: 
---
def left():
  motor_l.start(50)
  motor_r.start(50)


def right():
  motor_l.start(-50)
  motor_r.start(-50)


--- /code ---

--- /task ---

--- task ---

To test your code, you can edit your `for` loop.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 32
line_highlights: 
---
for i in range(2):
  forward()
  sleep(1)
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

