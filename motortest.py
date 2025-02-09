print('motor test')
import RPi.GPIO as GPIO
import time

# print("GPIO Version", GPIO.__version__)

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


print('motor 1 forward')
motor1_forward.ChangeDutyCycle(100)

time.sleep(1)
print('motor 1 backward')

motor1_forward.ChangeDutyCycle(0)
motor1_backward.ChangeDutyCycle(100)
time.sleep(1)
print('motor 2 forward')
motor1_backward.ChangeDutyCycle(0)
motor2_forward.ChangeDutyCycle(100)

time.sleep(1)
print('motor 2 backward')
motor2_forward.ChangeDutyCycle(0)
motor2_backward.ChangeDutyCycle(100)

time.sleep(1)
print('motor 3 forward')
motor2_backward.ChangeDutyCycle(0)
motor3_forward.ChangeDutyCycle(100)
time.sleep(1)

print('motor 3 backward')
motor3_forward.ChangeDutyCycle(0)
motor3_backward.ChangeDutyCycle(100)

time.sleep(1)
print('motor 4 forward')
motor3_backward.ChangeDutyCycle(0)
motor4_forward.ChangeDutyCycle(100)
time.sleep(1)

print('motor 4 backward')
motor4_forward.ChangeDutyCycle(0)
motor4_backward.ChangeDutyCycle(100)

time.sleep(1)
print('stopping')
motor2_forward.ChangeDutyCycle(0)
motor2_backward.ChangeDutyCycle(0)
motor1_forward.ChangeDutyCycle(0)
motor1_backward.ChangeDutyCycle(0)
motor3_forward.ChangeDutyCycle(0)
motor3_backward.ChangeDutyCycle(0)
motor4_forward.ChangeDutyCycle(0)
motor4_backward.ChangeDutyCycle(0)


# time.sleep(100000)

time.sleep(5)

print("stopped");


GPIO.cleanup()
