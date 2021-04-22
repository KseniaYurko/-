import RPi.GPIO as GPIO
import time

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

def num2dac(val):
    binary = bin(val)[2:].zfill(8)
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
DarkALL()

GPIO.setup(4, GPIO.IN)
GPIO.output(17, 1)

try:        
        while True:
            value = int(input("Print value (-1 to exit) "))

            if value == -1:
                break
        
            if value < 0 or value > 255:
                raise Exception
                
            a = num2dac(value)
            time.sleep(0.001)
            if GPIO.input(4) == 0:
                print(a, "-", (round(value*3.26/255*100))/100, "V")
                

except ZeroDivisionError:
    print('Число от 0 до 255!!!')
except ValueError:
    print('Число от 0 до 255!!!')

finally:
    DarkALL()
    GPIO.cleanup()