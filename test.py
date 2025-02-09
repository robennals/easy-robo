from mecanum import makeMotorVector, driveMotors
import time

print("forward")
driveMotors(makeMotorVector(1,0,0))
time.sleep(2)

print("backward")
driveMotors(makeMotorVector(-1,0,0))
time.sleep(2)

print("left")
driveMotors(makeMotorVector(0,1,0))
time.sleep(2)

print("right")
driveMotors(makeMotorVector(0,-1,0))
time.sleep(2)

print("turn left")
driveMotors(makeMotorVector(0,0,1))
time.sleep(2)

print("turn right")
driveMotors(makeMotorVector(0,0,-1))
time.sleep(2)



