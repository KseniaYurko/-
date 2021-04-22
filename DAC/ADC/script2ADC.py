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
    num2dac(128)
    if GPIO.input(17) == 1:
        print(1000000)
        while True:
            for j in range (0, 2**8):
                num2dac(j)
                time.sleep(0.001)
                if GPIO.input(4) == 0:
                    print(j, "-", (round(j*3.26/255*100))/100, "V")
                    break
  

except ZeroDivisionError:
    print('Число от 0 до 255!!!')
except ValueError:
    print('Число от 0 до 255!!!')

finally:
    DarkALL()
    GPIO.cleanup()

