import RPi.GPIO as GPIO
import time
import script1 as sc1

N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

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
                time.sleep(0.005)
                i+=1
           
                           
            while i>0:
                binary = sc1.num2dac(i)
                time.sleep(0.01)
                i-=1
          

finally:
    DarkALL()
    GPIO.cleanup()