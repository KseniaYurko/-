import RPi.GPIO as GPIO
import time

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)

def num2dac(val):
    binary = bin(val)[2:].zfill(8)
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))


def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)


if __name__ == '__main__':
    try:
        while True:
            value = int(input("Print value (-1 to exit) "))
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
        GPIO.cleanup()
        