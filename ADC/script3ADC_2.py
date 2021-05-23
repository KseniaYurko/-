import RPi.GPIO as GPIO
import time

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

def num2dac(val):

    binary = bin(val)[2:].zfill(8)
    binary = binary.replace("0b", '')
    binary = binary.replace("b", '')
    
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))


def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
DarkALL()

def binSearch():
    val = 0
    i = 128

    while True:
        
        num2dac(val)
        time.sleep(0.001)

        if GPIO.input(4) == 1:
            val += i
        
        else :
            val -= i

        i = int(i/2)
        
        if i == 0:
            break
         
    return (3.3*float(val) / 255)



try:

    GPIO.output(17, 1)

    Voltage = 0
    NewVoltage = 0

    while True:    
        NewVoltage = binSearch()
    
        if abs(NewVoltage - Voltage) > 1.0/255.0:
            print (round(NewVoltage, 2),' - ' , int(NewVoltage*255/3.3))
            Voltage = NewVoltage
finally:

    GPIO.output(N, 0)
    GPIO.output(17, 0)
    GPIO.cleanup()