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
GPIO.output(leds, 0)
GPIO.output(dac, 0)

def num2pins(pins, value):
    binary = [int (i) for i in bin(value)[2:].zfill(8)]
    GPIO.output(pins, binary)

def ADC():
    for i in range(255):
        num2pins(dac, i)
        time.sleep(0.001)
        
        if GPIO.input(comparator) == 0:
            return i

    return 255

try:
    GPIO.output(voltage3, 1)
    while True:
        print(ADC())

finally:
    GPIO.cleanup()