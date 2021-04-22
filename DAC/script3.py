import RPi.GPIO as GPIO
import time
import script1 as sc1
import numpy as np
import matplotlib.pyplot as plt



N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

frequency = int(input('Частота: '))
timee = int(input('Время: '))
SF = int(input('Частота дискредитации: '))

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)

try:
    x = np.linspace(0, timee, SF)
    y = 255*(np.sin(2*np.pi*frequency*x))
    y_new = np.round(y,0)
    y_final = y_new.astype(np.int32)
    
    fig = plt.subplots()
  
    for i in y_final:
        a = sc1.num2dac(i) 
        time.sleep(1/SF)
    plt.plot(x, y(x))
    plt.show()

finally:
    DarkALL()
    GPIO.cleanup()