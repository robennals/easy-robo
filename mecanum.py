# [front-left, back-left, front-right, back-right]

from motor import moveMotor1, moveMotor2, moveMotor3, moveMotor4

forwardVec = [1,1,1,1]
leftVec = [-1,1,1,-1]
turnVec = [-1,-1,1,1]

def driveMotors(powerVec):
    moveMotor1(powerVec[0])
    moveMotor2(powerVec[1])
    moveMotor3(powerVec[2])
    moveMotor4(powerVec[3])

def stopMotors():
    driveMotors([0,0,0,0])

def combinePower(index, forward, left, turn):
    divisor = max(abs(forward) + abs(left) + abs(turn),1)
    return (forwardVec[index]*forward + leftVec[index]*left + turnVec[index]*turn)/divisor

def makeMotorVector(forward, left, turn):
    return [
        combinePower(0, forward, left, turn), 
        combinePower(1, forward, left, turn), 
        combinePower(2, forward, left, turn), 
        combinePower(3, forward, left, turn), 
    ]
