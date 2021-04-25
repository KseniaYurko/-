import RPi.GPIO as GPIO
import time
import script1 as sc1
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

SOUND = '/home/pi/Downloads/SOUND.WAV'

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)

def num2dac(val):
    binary = bin(val)[2:].zfill(8)
    for i in range(8):
        GPIO.output(N[i], int(binary[7 - i]))


try:
    #[SF, data] = wavfile.read(SOUND)
    #print(SF, ' -Частота дискретизации')
    #print(data, ' - данные')
    #length = len(data)
    #print(length, ' -длина')
    #max_y = np.max(data)
    #step = int(round((2*max_y)/256))
    #print (max_y, ' -максимум')
    #print (step, ' -шаг')

    data = float(1)
    SF, data = wavfile.read(SOUND) 
    print("SF = ",SF)

    timee = len(data) / float(SF)
    print("Длительность = ", timee) 
    y = data[:,0]
    print(y)
    x = np.arange(0, timee, 1/SF)
    print(x)

    for i in range (round(timee)*SF):
        num2dac(round(255 * abs(y[i])))
        time.sleep(1/SF)

    plt.plot(x, y)
    plt.show()

finally:    
    DarkALL()
    GPIO.cleanup()