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
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)
DarkALL()

GPIO.setup(4, GPIO.IN)
GPIO.output(17, 1)

try:
    
    voltage = 0
    newVoltage = 0
    
    while True:
    
        for i in range (0, 255):
            num2dac (i)
            time.sleep (0.0001)

            if GPIO.input (4) != 1:
                newVoltage = 3.3*float(i)/255
                break
    
        if abs(newVoltage - voltage) > 1.0/255.0:
            print (round(newVoltage, 2),' - ' , int(newVoltage*255/3.3))
            voltage = newVoltage
  

except ZeroDivisionError:
    print('Число от 0 до 255!!!')
except ValueError:
    print('Число от 0 до 255!!!')

finally:
    DarkALL()
    GPIO.cleanup()

