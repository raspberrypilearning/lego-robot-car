from buildhat import Motor
from bluedot import BlueDot
from signal import pause
from gpiozero import LED

motor_left = Motor('A')
motor_right = Motor('B')
led_left = LED(20)
led_right = LED(21)
bd = BlueDot()


def stop():
    motor_left.stop()
    motor_right.stop()
    led_right.on()
    led_left.on()

def forward():
    motor_left.start(-100)
    motor_right.start(100)
    led_right.off()
    led_left.off()


def backward():
    motor_left.start(100)
    motor_right.start(-100)
    led_right.on()
    led_left.on()

def right():
    motor_left.start(-100)
    motor_right.start(-100)
    led_right.blink()
    led_left.off()

def left():
    motor_left.start(100)
    motor_right.start(100)
    led_right.off()
    led_left.blink()

def move(pos):
    if pos.top:
        forward()
    elif pos.bottom:
        backward()
    elif pos.left:
        left()
    elif pos.right:
        right()


bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
pause()
