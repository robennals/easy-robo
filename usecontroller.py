import controller
import motor
from controller import eventLoop
from motor import motorForward, motorBackward, moveMotor1, moveMotor2

print('hello')

def onButton(button, value):
    print('button', button, value)

def onStick(stick, value):
    print('stick', stick, value)
    if stick == 'stick1-Y':
        moveMotor1(value)
    elif stick == 'stick2-Y':
        moveMotor2(-value)

eventLoop(onButton, onStick)
