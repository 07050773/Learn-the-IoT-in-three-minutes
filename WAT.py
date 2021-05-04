def wat():
    #!/usr/bin/env python3
    import time
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(22, GPIO.OUT,initial=GPIO.LOW) #GPIO 23

    #GPIO = 23
    #try:
    #if DHT22 > 25
       #print('按下 Ctrl-C 可停止程式')
    #while True:
    #if :
    time.sleep(5)
    print('WAT ON !')
    GPIO.output(22,True)
    #else:
    time.sleep(10)
    print('WAT OFF !')
    GPIO.output(22,False)
    time.sleep(10)
    #except KeyboardInterrupt:
    #print('關閉程式')

