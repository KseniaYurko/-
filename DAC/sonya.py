try:
    import RPi.GPIO as GPIO
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    from os.path import dirname, join as pjoin
    from scipy.io import wavfile as wav
    import scipy.io
except ImportError:
    print ("Import libraries error!")
    raise SystemExit
 
try:
    chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (chan_list, GPIO.OUT)
except:
    print ("Initialization  GPIO error!")
    raise SystemExit
 
bin_depth = 8
 
def decToBinList (value):
	#if value < 0 or value > 255:
	#	print ("Value error!")
    p = 0
    N = bin_depth - 1
    X = []
    while N > 0:
        p = int(value/ 1<<N)
        if p == 1:
            X.append(1)
            value -= 1<<N 
        else:
            X.append(0)
        N -= 1
    X.append(value)
    return X
 
def num2dac (value):
    x = decToBinList (value)
    GPIO.output (chan_list, x)

SOUND = '/home/pi/Downloads/SOUND.WAV'

data_dir = pjoin(dirname(__file__))

samplerate, data = wav.read(SOUND)
length = data.shape[0] / samplerate

print ("длина: ", int(length), "s, номер канала: ", data.shape[1], ", частота дискретизации: ", samplerate, ", тип данных: ", type (data[1, 0]))

try:
    for i in data[:, 0]:
        num2dac ((int(i) + 16384) / 256)
except ValueError:
    print ("Ошибка в в размере входных данных. Выходим из программы")
except:
    print ("Неизвестная ошибка. Выходим из программы")
finally:
    GPIO.output (chan_list, 0)
    GPIO.cleanup (chan_list)



        #[SF, data] = wavfile.read(SOUND)
    #print(SF, ' -Частота дискретизации')
    #print(data, ' - данные')
    #length = len(data)
    #print(length, ' -длина')
    #max_y = np.max(data)
    #step = int(round((2*max_y)/256))
    #print (max_y, ' -максимум')
    #print (step, ' -шаг')
