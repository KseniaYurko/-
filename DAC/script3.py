import RPi.GPIO as GPIO
import time
import script1 as sc1
import numpy as np
import matplotlib.pyplot as plt



N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

frequency = 200
timee = 10

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)

try:
    y = lambda x: 255*(np.sin(2*np.pi*frequency*x))
    fig = plt.subplots()
    x = np.linspace(0, timee, 1000)
    
    for i in x:
        print(y)
      #  y = sc1.num2dac(i) 
       # time.sleep(0.005)
      #  GPIO.output(4,0)
      #  time.sleep(0.0048)
      #  GPIO.output(4,1)
      #  time.sleep(0.0002) 
    plt.plot(x, y(x))
    plt.show()

finally:
    DarkALL()
    GPIO.cleanup()