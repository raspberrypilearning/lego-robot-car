from buildhat import Motor
from bluedot import BlueDot
from signal import pause
from gpiozero import LED

motor_links = Motor('A')
motor_rechts = Motor('B')
dot = BlueDot()
led_links = LED(20)
led_rechts = LED(21)


def stop():
    motor_links.stop()
    motor_rechts.stop()
    led_rechts.on()
    led_links.on()


def vorwaerts():
    motor_links.start(-100)
    motor_rechts.start(100)
    led_rechts.off()
    led_links.off()


def zurueck():
    motor_links.start(100)
    motor_rechts.start(-100)
    led_rechts.on(0.2)
    led_links.on(0.2)


def rechts():
    motor_links.start(-100)
    motor_rechts.start(-100)
    led_rechts.blink(0.2)
    led_links.off()


def links():
    motor_links.start(100)
    motor_rechts.start(100)
    led_rechts.off()
    led_links.blink(0.2)


def bewege(pos):
    if pos.top:
        vorwaerts()
    elif pos.bottom:
        zurueck()
    elif pos.left:
        links()
    elif pos.right:
        rechts()


dot.when_pressed = move
dot.when_released = stop
dot.when_moved = move

pause()
