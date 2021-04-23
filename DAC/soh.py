import RPi.GPIO as GPIO
import time
import math
import numpy as np
import matplotlib.pyplot as plt


GPIO.setmode(GPIO.BCM)

leds = [10,9,11,5,6,13,19,26]

GPIO.setup(leds,GPIO.OUT)

from script1 import num2dac
from script1 import lightMas

pi2 = 2 * math.pi

frequency = 2

Pe = 1 / frequency

samplingFrequency = 10

samPe = 1 / samplingFrequency

tim = int (input ("Введите время в миллисекундах: "))

mas = np.zeros(tim)


for i in range(tim):
    someTime= i / samPe / 1000

    nCol = math.ceil(someTime)

    samplingPerion = nCol * samPe * 1000

    pp = math.sin((samplingPerion - 1) * pi2 / Pe / 1000 )

    value = math.ceil((pp + 1) * 128) - 1
    mas[i] = value
    a = num2dac(value)
    lightMas(a)

    print(someTime, nCol, pp, value)

    time.sleep(1/1000)


tt = np.arange(0, tim, 1)
plt.plot(tt, mas)
plt.xlabel('Время в миллисекундах')
plt.ylabel('Напряжение в процентах от MAX')
plt.show()
time.sleep(1)
plt.close()

GPIO.output(leds,0)
GPIO.cleanup()