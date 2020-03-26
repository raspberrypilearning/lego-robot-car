## Setting up the Motors

It is easier to test and develop your program before building your robot. This reduces the risk of ruining your wonderful model when a motor unexpectedly sends the robot in the wrong direction and it careens off your desk (although, of course, the good thing about using LEGO is that you always rebuild).

The Raspberry Pi LEGO HAT and its Python library allow you to control LEGO Technic motors directly from your Raspberry Pi computer.

Plug two motors into ports A and B on the Raspberry Pi LEGO HAT.  

### Make the motors spin

Open up your favourite Python editor and enter the code below to import the LEGO HAT library and the sleep function from the time library (which we'll use later) and make both motors move for 1000ms at 50% of the maximum speed possible.

```python
from spike import SPIKEPrimeSerial as SPIKE
from time import sleep

mySPIKE = SPIKE()
mySPIKE.OpenSerial(port = "/dev/ttyACM0")
mySPIKE.OpenSerial()
mySPIKE.SendCommand("hub.port.B.motor.run_for_time(1000,50)")
mySPIKE.SendCommand("hub.port.A.motor.run_for_time(1000,-50)")
```

Run your program and check the motors turn. When testing it can be helpful to add some LEGO to the central axle hole in the motor so that it is easy to see the direction the motor is turning.

Your current program should move the motors in opposite directions? Why is this necessary?

--- hints ---


--- hint ---

Because this will be a differential wheeled robot,  the identical motors identical will be mounted on opposite sides of the robot chassis. So anti-clockwise rotation on the left hand wheel will move the robot forward, whereas a clockwise rotation is needed on the right hand side.

--- /hint ---

--- /hints ---

In order to remotely steer the robot, you'll need to be able to start and stop the motors rather than just have them move for a set time.   Create two functions, one to cause the robot to move forward and another to stop.

```python
def stop():
  mySPIKE.SendCommand("hub.port.A.motor.brake()")
  mySPIKE.SendCommand("hub.port.B.motor.brake()")

def forward():
  mySPIKE.SendCommand("hub.port.B.motor.run_at_speed(50)")
  mySPIKE.SendCommand("hub.port.A.motor.run_at_speed(-50)")

```

Test you functions out by adding the following start-stop-start-stop sequence:

```python

for i in range(2):
  forward()
  sleep(1)
  stop()
  sleep(1)
```

Once that works, add 3 more functions to move the robot backwards, left and right.

--- hints ---


--- hint ---

To move the robot backwards, simply reverse the directions of both motors.

```python
def back():
  mySPIKE.SendCommand("hub.port.B.motor.run_at_speed(-50)")
  mySPIKE.SendCommand("hub.port.A.motor.run_at_speed(50)")

```

--- /hint ---

--- hint ---

To turn the robot to the left, both motors need to turn in the same direction.

```python
def left():
  mySPIKE.SendCommand("hub.port.B.motor.run_at_speed(50)")
  mySPIKE.SendCommand("hub.port.A.motor.run_at_speed(50)")

```

You'll need to think about which side of the robot each motor will be on to work out which direction to turn them.

--- /hint ---

Finally, to turn the robot to the right, both motors need to turn in the same (opposite) direction.

```python
def right():
  mySPIKE.SendCommand("hub.port.B.motor.run_at_speed(-50)")
  mySPIKE.SendCommand("hub.port.A.motor.run_at_speed(-50)")

```


--- /hint ---

--- /hints ---
