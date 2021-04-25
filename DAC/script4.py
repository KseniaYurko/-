import RPi.GPIO as GPIO
import time
import script1 as sc1
from scipy.io import wavfile
import scipy.io
import numpy as np
import math
import matplotlib.pyplot as plt

N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

SOUND = '/home/pi/Downloads/SOUND.WAV'

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)

def decToBinList (decNumber):
    if decNumber < 0 or decNumber > 255:
        raise ValueError
    return [(int(decNumber) & (1 << i)) >> i for i in range (7, -1, -1)]

def num2dac (value):
    x = decToBinList (value)
    GPIO.output (N, tuple (x))


try:

    data = float(1)
    SF, data = wavfile.read(SOUND) 
    print("Частота дискретизации = ",SF)

    timee = len(data) / float(SF)
    print("Длительность = ", timee) 
    
    y = data[:, 0]
    x = np.arange(0, timee, 1/SF)
    max_y = int(np.max(y))
    min_y = int(np.min(y))
    print (max_y, ' -максимум')
    print (min_y, ' -минимум')
    
    for i in y:

        num2dac((int(i) + 32768) / 256)

        time.sleep(1/SF)
        GPIO.output(4,0)
        GPIO.output(4,1)

finally:    
    DarkALL()
    GPIO.cleanup()