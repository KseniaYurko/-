import RPi.GPIO as GPIO
import time
import script1 as sc1

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)

repetitionsNumber = (int(input('Введите число повторений: ')))
i = 0

try: 
    for j in range (rprtitionsNumber):
            
            while i<=255:
                binary = sc1.num2dac(i) 
                GPIO.output(N, binary)
                time.sleep(0.01)
                i+=1
            
            while i>=0:
                binary = sc1.num2dac(i)
                GPIO.output(N, binary)
                time.sleep(0.01)
                i-=1
finally:
    DarkALL()
    GPIO.cleanup()