from buildhat import Motor
from bluedot import BlueDot
from signal import pause
from gpiozero import LED

motor_izquierda = Motor ('A')
motor_derecha = Motor ('B')
dot = BlueDot()
led_izquierda = LED(20)
led_derecha = LED(21)


def detener():
    motor_izquierda.stop()
    motor_derecha.stop()
    led_derecha.on()
    led_izquierda.on()


def avanzar():
    motor_izquierda.start(-100)
    motor_derecha.start(100)
    led_derecha.off()
    led_izquierda.off()


def atras():
    motor_izquierda.start(100)
    motor_derecha.start(-100)
    led_derecha.on(0.2)
    led_izquierda.on(0.2)


def derecha():
    motor_izquierda.start(-100)
    motor_derecha.start(-100)
    led_derecha.blink(0.2)
    led_izquierda.off()


def izquierda():
    motor_izquierda.start(100)
    motor_derecha.start(100)
    led_derecha.off()
    led_izquierda.blink(0.2)


def mover(pos):
    if pos.top:
        avanzar()
    elif pos.bottom:
        atras()
    elif pos.left:
        izquierda()
    elif pos.right:
        derecha()


dot.when_pressed = move
dot.when_released = stop
dot.when_moved = move

pause()
