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
timee = int(input('Время выполнения программы: : '))
SF = int(input('Частота дискредитации: '))

def DarkALL():
    for i in range(8):
        GPIO.output(N[i], 0)

try:
    x = np.linspace(0, timee, num = SF)
    y = 127*(np.sin(2*np.pi*frequency*x))+127
    fig = plt.subplots()

    y_new = np.round(y,0)
    y_final = y_new.astype(np.int32)    

    print(x)
    print(y_final)

    timeout = time.time() + timee

    while True:
        if time.time()>timeout:
            break
        
        for i in y_final:
 
            y_final_new = sc1.num2dac(i)      
            time.sleep(1/SF)
            GPIO.output(4,0)
            GPIO.output(4,1)

    plt.plot(x, y_final)
    plt.show()

finally:    
    DarkALL()
    GPIO.cleanup()