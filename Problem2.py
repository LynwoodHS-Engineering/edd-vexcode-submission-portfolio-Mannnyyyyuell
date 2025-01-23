from vex import *

brain=Brain()

bumperA = Bumper(brain.three_wire_port.a)
bumperB = Bumper(brain.three_wire_port.b)
redLed = Led(brain.three_wire_port.c)
greenLed = Led(brain.three_wire_port.d)


while True:

    if bumperA.pressing() and bumperB.pressing():
        greenLed.on()
        redLed.off()

   
    else:
        greenLed.off()
        redLed.on()

    wait(20, MSEC)
