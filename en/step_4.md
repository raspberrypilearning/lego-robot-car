## Control your motors with Blue Dot

Now modify your code from the previous step so that the movement sequence is triggered by a press of the blue dot.

--- hints ---


--- hint ---

You don't need to make any changes to the function you wrote before. That's the cool thing about making your code modular with functions.


--- /hint ---

--- hint ---

The `bd.wait_for_press()` function will pause the execution of your program until it receives a message via Bluetooth to say the button has been pressed.



--- /hint ---
```python
from bluedot import BlueDot
bd = BlueDot()
from buildhat import Motor
from time import sleep

motor_l = motor('A')
motor_r = motor('B')

def stop():
  motor_l.stop()
  motor_r.stop()

def forward():
  motor_l.start(50)
  motor_r.start(-50)

def back():
  motor_l.start(-50)
  motor_r.start(50)

def left():
  motor_l.start(50)
  motor_r.start(50)

def right():
  motor_l.start(-50)
  motor_r.start(-50)

print('Waiting...')
bd.wait_for_press()
print("It worked!")
forward()
sleep(1)
stop()
sleep(1)

```

--- /hint ---

--- /hints ---

### More than just a blue dot

The Blue Dot app is more than just a simple button. The blue dot itself can also be used as a joystick when the middle, top, bottom, left or right areas of the dot are touched. You can use this to steer the robot using the blue dot.

Modify your existing code to move the robot backwards and forwards using the blue dot. Add the following new function:


```python
def move(pos):
    if pos.top:
        forward()
    elif pos.bottom:
        back()

```


```python
from bluedot import BlueDot
from signal import pause

bd = BlueDot()

def move(pos):
    if pos.top:
        robot.forward()
    elif pos.bottom:
        robot.backward()
    elif pos.left:
        robot.left()
    elif pos.right:
        robot.right()

def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop

pause()
```

You can change the robot to use variable speeds, so the further towards the edge you press the Blue Dot, the faster the robot will go.

The distance attribute returns how far from the centre the Blue Dot was pressed, which can be passed to the robot’s functions to change its speed:
