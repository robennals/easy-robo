import controller
import motor
from controller import eventLoop, connectToController
from motor import motorForward, motorBackward, moveMotor1, moveMotor2
import time
from mecanum import makeMotorVector, driveMotors

left = 0
forward = 0
turn = 0

# def doHelloDance():
#     moveMotor1(1)
#     moveMotor2(1)
#     time.sleep(1)
#     moveMotor1(-1)
#     moveMotor2(-1)
#     time.sleep(1)
#     moveMotor1(0)
#     moveMotor2(0)

# print('Starting: Drive Robot')

# doHelloDance()

connectToController()
print('Connected to Controller')

    
# doHelloDance()

print('Ready to drive!')


x = 0
y = 0

def onButton(button, value):
    print('button', button, value)

def clipValue(value):
    return min(1, max(-1, value))

def setMotors():
    # print('values', forward, left, turn)
    vec = makeMotorVector(forward, left, turn)
    driveMotors(vec)
    # moveMotor1(clipValue(y - x))
    # moveMotor2(-clipValue(y + x))

def onStick(stick, value):
    # print('stick', stick, value)
    global forward
    global left
    global turn
    if stick == 'stick1-Y':
        forward = -value
        setMotors()
    elif stick == 'stick1-X':
        left = -value
        setMotors()
    elif stick == 'stick2-X':
        turn = -value
        setMotors()

eventLoop(onButton, onStick)
