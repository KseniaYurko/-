import RPi.GPIO as GPIO
import time
import script1 as sc1

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)

repNum = (int(input('Введите число повторений: ')))
i = 0

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
DarkALL()

try: 
    for j in range (repNum):
            
            while i<=255:
                binary = sc1.num2dac(i) 
                time.sleep(0.001)
                print(i)
                i+=1
            
            while i>0:
                binary = sc1.num2dac(i)
                time.sleep(0.001)
                print(i)
                i-=1

finally:
    DarkALL()
    GPIO.cleanup()