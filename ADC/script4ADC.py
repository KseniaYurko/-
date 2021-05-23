import RPi.GPIO as GPIO
import time

N = [26, 19, 13,  6,  5, 11,  9, 10]
M = [21, 20, 16, 12, 7, 8, 25, 24]
RC_PIN = 17
CMP_PIN = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(RC_PIN, GPIO.OUT)
GPIO.setup(N, GPIO.OUT) 
GPIO.setup(M, GPIO.OUT) 
GPIO.setup(CMP_PIN, GPIO.IN)
GPIO.output(17, 1)

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)


def num2dac(val):

    binary = bin(val)[2:].zfill(8)
    binary = binary.replace("0b", '')
    binary = binary.replace("b", '')
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))


def binSearch():
    val = 0
    step = 128

    while True:
        
        num2dac(val)
        time.sleep(0.001)

        if GPIO.input(4) == 0:
            val += step
        
        else :
            val -= step

        step = int(step/2)
        
        if step == 0:
            break

    return (val)   


def num2VolLvl(number):
    
    num2dac(number)
    LEVEL = [0, 0, 0, 0, 0, 0, 0, 0]
    
    if number > 252:
        LEVEL = [1, 1, 1, 1, 1, 1, 1, 1]
        led = 8

    elif (number > (256/8*7)):
        LEVEL = [0, 1, 1, 1, 1, 1, 1, 1]
        led = 7
        
    elif (number > (256/8*6)):
        LEVEL  = [0, 0, 1, 1, 1, 1, 1, 1]
        led = 6
        
    elif (number > (256/8*5)):
        LEVEL  = [0, 0, 0, 1, 1, 1, 1, 1]
        led = 5
        
    elif (number > (256/8*4)):
        LEVEL  = [0, 0, 0, 0, 1, 1, 1, 1]
        led = 4
        
    elif (number > (256/8*3)):
        LEVEL  = [0, 0, 0, 0, 0, 1, 1, 1]
        led = 3
        
    elif (number > (256/8*2)):
        LEVEL  = [0, 0, 0, 0, 0, 0, 1, 1]
        led = 2
        
    elif (number > (256/8*1)):
        LEVEL  = [0, 0, 0, 0, 0, 0, 0, 1]
        led = 1
        
    else:
        LEVEL  = [0, 0, 0, 0, 0, 0, 0, 0]
        led = 0

    GPIO.output(M, LEVEL)
        

try:
    GPIO.output(17, 1)
    while True:       
        val = binSearch()

        a = round((3.3*float(val) / 255), 2)
        print(a)
        lev = num2VolLvl(val)

finally:
    GPIO.output(N, 0)
    GPIO.output(M, 0)
    GPIO.output(17, 0)
    GPIO.cleanup()