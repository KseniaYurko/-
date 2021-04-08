# -

import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
import numpy as np

outs = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(outs, GPIO.OUT)

try:
    time = np.arange(0, 20, 0.1)
    amplitude = np.sin(time)
    plt.plot(time, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()
