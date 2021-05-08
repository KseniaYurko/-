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
val = 10000000

try:


        list_val = list(str(val))
        for i in range(7):
            
            if GPIO.input(4) == 0:
                
                list_val.insert(i, 1)
                list_val.pop(8)

            if GPIO.input(4) == 1:
            
                list_val.insert(i, 0)
                list_val.pop(8) 

            list_val_int = [int(x) for x in list_val]
            print(list_val_int)
            for i in range (7):
                GPIO.output(N[i],list_val_int[i])          
            
        result = int(''.join(map(str, list_val)))
        print(result)
        Fres = int(str(result), base=2)
        print(Fres)
        print(Fres, "-", (round(Fres*3.26/255*100))/100, "V")

except ZeroDivisionError:
    print('Число от 0 до 255!!!')
except ValueError:
    print('Число от 0 до 255!!!')

finally:
    DarkALL()
    GPIO.cleanup()
