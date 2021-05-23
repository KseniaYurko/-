def binSearch():
    
    val = 0
    step = 128

    for i in range(8):  
        num2dac(val)
        time.sleep(0.001)

        if GPIO.input(4) == 1:
            val += step
            print('step', i, ' - мало: добавляем ', step, ' - ', val)
            time.sleep(0.8)

        if GPIO.input(4) == 0:
            val -= step
            print('step', i, ' - много: вычитаем ', step, ' - ', val)
            time.sleep(0.8)
        step = int(step/2)     
    print(val)
    volt = (round((3.3*float(val) / 255), 2)) 
    print(volt, ' - ', type(volt))   
    return(volt)   