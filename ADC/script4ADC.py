import RPi.GPIO as GPIO
import time

N = [26, 19, 13,  6,  5, 11,  9, 10]
RC_PIN = 17
CMP_PIN = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(RC_PIN, GPIO.OUT)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(CMP_PIN, GPIO.IN)

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)


def num2dac(val):
    binary = bin(val)[2:].zfill(8)
    for i in range(8): 
        GPIO.output(N[i], int(binary[7 - i]))


def binSearch():
    val = 0
    i = 128

    while True:
        num2dac(val)
        time.sleep(0.001)

        if GPIO.input(CMP_PIN) == 1:
            val += i
        
        else :
            val -= i

        i = int(i / 2)
        if i == 0:
            break

    if value < 0:
        return 0
    return (3.3*float(val) / 255)        


def num2VolLvl(number) :
    LEVEL = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if (number >= 252):
        LEVEL = [1, 1, 1, 1, 1, 1, 1, 1]

    elif (number > (256/8*7)):
        LEVEL = [0, 1, 1, 1, 1, 1, 1, 1]

    elif (number > (256/8*6)):
        LEVEL  = [0, 0, 1, 1, 1, 1, 1, 1]

    elif (number > (256/8*5)):
        LEVEL  = [0, 0, 0, 1, 1, 1, 1, 1]

    elif (number > (256/8*4)):
        LEVEL  = [0, 0, 0, 0, 1, 1, 1, 1]

    elif (number > (256/8*3)):
        LEVEL  = [0, 0, 0, 0, 0, 1, 1, 1]

    elif (number > (256/8*2)):
        LEVEL  = [0, 0, 0, 0, 0, 0, 1, 1]

    elif (number > (256/8*1)):
        LEVEL  = [0, 0, 0, 0, 0, 0, 0, 1]

    else:
        LEVEL  = [0, 0, 0, 0, 0, 0, 0, 0]

    GPIO.output(N, 0)

    for i in range (0, 8) :
        if LEVEL[i] == 1 :
            GPIO.output(N[7 - i], 1)

GPIO.output(RC_PIN, 1)
val = 0

while True:
    
    val = binSearch()
    num2VolLvl(val)
    print(val)

GPIO.output(N, 0)
GPIO.output(RC_PIN)
GPIO.cleanup()