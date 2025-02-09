import evdev
from evdev import InputDevice, categorize, ecodes
import time

controller_path = '/dev/input/event2'
controller = None

# Loop until the controller is connected
def connectToController():
    global controller
    while controller is None:
        try:
            controller = InputDevice(controller_path)
            print("Controller connected!")
        except (FileNotFoundError, PermissionError):
            print("Controller not found. Retrying in 1 second...")
            time.sleep(1)

buttonNames = {
    304: 'A',
    305: 'B',
    308: 'X',
    307: 'Y',
    313: 'RB',
    311: 'RT',
    310: 'LT',
    312: 'LB',
    316: 'home',
    315: 'start',
    16: 'pad-X',
    17: 'pad-Y',
    3: 'stick2-X',
    4: 'stick2-Y',
    0: 'stick1-X',
    1: 'stick1-Y',
    5: 'stick3-Y',
    2: 'stick3-X'
}

def eventLoop(onButton, onStick):
    global controller
    for event in controller.read_loop():
        if event.type in [ecodes.EV_KEY, ecodes.EV_ABS] :
            if event.code <= 5 and event.code in buttonNames:
                # print('Stick Event', buttonNames[event.code], event.value)
                onStick(buttonNames[event.code], event.value / 32767)
            elif event.code in buttonNames:
                # print('Button Event', buttonNames[event.code], event.value)
                onButton(buttonNames[event.code], event.value / 32767)
            # else:
                # print('Unknown ', event.code)
