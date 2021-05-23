import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
import os

path = r'/home/pi/ADC' 
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
voltage3 = 17
comparator = 4
file = 'NUM.txt'

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds + dac, GPIO.OUT)
GPIO.setup(voltage3, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)

GPIO.output(leds, 0)
GPIO.output(dac, 0)

def num2pins(pins, value):
    binary = [int (i) for i in bin(value)[2:].zfill(8)]
    GPIO.output(pins, binary)

def binADC():

    value = 0
    direction = 1

    for i in range(8):
        delta = 2**(8-i-1)
        value += delta*direction

        num2pins(dac, value)
        time.sleep(0.001)

        if GPIO.input(comparator) == 0:
            direction = -1
        else:
            direction = 1
    return value
            
def level():
    LEVEL =[0]*8
    value = binADC()
    numLEV = round(value/32)  

    for i in range(numLEV):
        LEVEL.insert(0, 1)
        LEVEL.pop(8)
    
    GPIO.output(leds, LEVEL)
    return numLEV


def mainCODE():
    n = 0
    with open(os.path.join(path,'NUM.txt'), 'w') as counter_file:
        counter_file.write(str(n))
        counter_file.close()

    file = 'data{}.txt'.format(n)
    open(os.path.join(path, file), "w")
    
    GPIO.output(voltage3, 1)
    timeline = []
    measure = []
    delta = time.time()
    value = 0


    while True:
        while value <= 251:
            file.wl('Зарядка:')

            value = binADC()
            measure.append(round((value*3.26/255), 2))
            timeline.append(round(time.time()-delta, 2))
            
            file.wl(round((value*3.26/255), 2), ' - voltage',round(time.time()-delta, 2), ' - time')
            
            print(value, '', round((value*3.26/255), 2),'V')
            level()

        while value > 1:
            file.wl('Разрядка:')

            GPIO.output(voltage3, 0)
            value = binADC()
            measure.append(round((value*3.26/255), 2))
            timeline.append(round(time.time()-delta, 2))

            file.wl(round((value*3.26/255), 2), ' - voltage',round(time.time()-delta, 2), ' - time')

            print(value, '', round((value*3.26/255), 2),'V')
            level()

        if value == 1:
            break
    
    plt.plot(timeline, measure)
    plt.title('График зарядки и разрядки конденсатора')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.show()
    time.sleep(10)
    plt.close()
    
    np.savetxt('data{}.txt'.format(n), measure, fmt='%d')
    n += 1


try:
    os.mkdir(path)
    mainCODE()

except FileExistsError:
    mainCODE()

finally:
    GPIO.cleanup()