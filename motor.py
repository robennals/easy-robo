print('motor test')
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


motor1_forward = GPIO.PWM(21, 100)
motor1_backward = GPIO.PWM(20, 100)
motor2_forward = GPIO.PWM(16, 100)
motor2_backward = GPIO.PWM(26, 100)
motor3_forward = GPIO.PWM(19, 100)
motor3_backward = GPIO.PWM(13, 100)
motor4_forward = GPIO.PWM(6, 100)
motor4_backward = GPIO.PWM(5, 100)

motor1_forward.start(0)
motor1_backward.start(0)
motor2_forward.start(0)
motor2_backward.start(0)
motor3_forward.start(0)
motor3_backward.start(0)
motor4_forward.start(0)
motor4_backward.start(0)


print('started motor')

def moveMotor1(amount):
    if amount > 0.1:
        motor1_forward.ChangeDutyCycle(amount * 100)
        motor1_backward.ChangeDutyCycle(0)
    elif amount < -0.1:
        motor1_backward.ChangeDutyCycle(-amount * 100)
        motor1_forward.ChangeDutyCycle(0)
    else:
        motor1_forward.ChangeDutyCycle(0)
        motor1_backward.ChangeDutyCycle(0)

def moveMotor2(amount):
    if amount > 0.1:
        motor2_forward.ChangeDutyCycle(amount * 100)
        motor2_backward.ChangeDutyCycle(0)
    elif amount < -0.1:
        motor2_backward.ChangeDutyCycle(-amount * 100)
        motor2_forward.ChangeDutyCycle(0)
    else:
        motor2_forward.ChangeDutyCycle(0)
        motor2_backward.ChangeDutyCycle(0)

def moveMotor3(amount):
    if amount > 0.1:
        motor3_forward.ChangeDutyCycle(amount * 100)
        motor3_backward.ChangeDutyCycle(0)
    elif amount < -0.1:
        motor3_backward.ChangeDutyCycle(-amount * 100)
        motor3_forward.ChangeDutyCycle(0)
    else:
        motor3_forward.ChangeDutyCycle(0)
        motor3_backward.ChangeDutyCycle(0)

def moveMotor4(amount):
    if amount > 0.1:
        motor4_forward.ChangeDutyCycle(amount * 100)
        motor4_backward.ChangeDutyCycle(0)
    elif amount < -0.1:
        motor4_backward.ChangeDutyCycle(-amount * 100)
        motor4_forward.ChangeDutyCycle(0)
    else:
        motor4_forward.ChangeDutyCycle(0)
        motor4_backward.ChangeDutyCycle(0)



def motorForward(amount):
    motor1_backward.ChangeDutyCycle(0)
    motor1_forward.ChangeDutyCycle(amount * 100)

def motorBackward(amount):
    motor1_forward.ChangeDutyCycle(0)
    motor1_backward.ChangeDutyCycle(amount * 100)
