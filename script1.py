import RPi.GPIO as GPIO
import time

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)
num = 8
timee = 0.05


def num2dac(val):
    binary = bin(val)[2:].zfill(num)
    for i in range(num):
        GPIO.output(N[i], int(binary[num - 1 - i]))


def DarkALL():
    for i in range(num):
        GPIO.output(N[i], 0)


if __name__ == '__main__':
    try:
        while True:
            value = int(input("Print value(-1 to exit)"))
            DarkALL()
            if value == -1:
                break
            if value < 0 or value > 255:
                raise Exception
            num2dac(value)
            time.sleep(0.3)
    finally:
        DarkALL()
        print("Quit")