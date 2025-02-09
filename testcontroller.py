from controller import eventLoop, connectToController

print('hello')

connectToController()
print('Connected to Controller')


def onButton(button, value):
    print('button', button, value)

def onStick(stick, value):
    print('stick', stick, value)

eventLoop(onButton, onStick)

print("done")
