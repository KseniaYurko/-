import numpy as np
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

N = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
def num2dac(val):
    binary = bin(val)[2:].zfill(8)
    binary = binary.replace("0b", '')
    binary = binary.replace("b", '')
    bin_list = list(str(binary))
    result_bin = []        
    
    for i in bin_list:        
        result_bin.append(int(i))
    bin_list = result_bin
    print(result_bin)
   
    for i in range(8):
        GPIO.output (N[i], result_bin[i])

num2dac(255)
time.sleep(5)
GPIO.cleanup()