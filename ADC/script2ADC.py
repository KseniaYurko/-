import RPi.GPIO as GPIO
import time

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.IN)

def num2dac(val):
    binary = bin(val)[2:].zfill(8)
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
DarkALL()

GPIO.setup(14, GPIO.IN)
GPIO.output(17, 1)

try:
    if GPIO.input(14) == 0:
        print(1000000)
        num2dac(128)
    
    while True:
            for j in range (0, 2**8):
                a =num2dac(j) 
                GPIO.output(4,1)
                GPIO.output(4,0)       
                time.sleep(0.0001)
                
                if GPIO.input(14) == 1:
                    print(j, "-", (round(j*3.26/255*100))/100, "V") 
                    
  

except ZeroDivisionError:
    print('Число от 0 до 255!!!')
except ValueError:
    print('Число от 0 до 255!!!')

finally:
    DarkALL()
    GPIO.cleanup()

