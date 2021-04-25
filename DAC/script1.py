import RPi.GPIO as GPIO
import time

N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def num2dac(val):
    binary = bin(val)[2:].zfill(8)
  
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))


def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
        GPIO.output(4, 0)       

try:
    while True:
        value = int(input("Print value (-1 to exit) "))
        DarkALL()
        if value == -1:
            break
        if value < 0 or value > 255:
            raise Exception
        a = num2dac(value)
        GPIO.output(4,1)
        GPIO.output(4,0)
        print(a)
        time.sleep(0.3)

finally:
    DarkALL()
    print("Quit")
    GPIO.cleanup()
        