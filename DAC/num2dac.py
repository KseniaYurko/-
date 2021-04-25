import RPi.GPIO as GPIO
import time

N = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)

c
    for i in range(8):
        GPIO.output(N[i], int(binary[num - 1 - i]))
num2dac(3)