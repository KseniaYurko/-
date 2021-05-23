import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
voltage3 = 17
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(voltage3, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

GPIO.output(leds + dac, 0)

def num2pins(pins, value):
    binary = [int (i) for i in (bin(value)[2:].zfill(8))]
    GPIO.output(pins, binary)

def binADC():
    
    value = 0
    direction = 1
    
    for i in range(8):
        delta = 2**(8-i-1)
        value += delta*direction

        num2pins(dac, value)
        time.sleep(0.001)

        if GPIO.input(comparator) == 0:
            direction = -1
        else:
            direction = 1
    return value

def level():
    LEVEL =[0]*8
    value = binADC()
    numLEV = round(value/32)  

    for i in range(numLEV):
        LEVEL.insert(0, 1)
        LEVEL.pop(8)
    
    GPIO.output(leds, LEVEL)
    return numLEV


try:
    GPIO.output(voltage3, 1)

    while True:
        level()
        value = binADC()
        print(value, '', round((value*3.26/255), 2),'V')

finally:
    GPIO.cleanup()