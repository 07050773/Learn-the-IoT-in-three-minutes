#!/usr/bin/env python3
pinFAN = 0

def fan():

  import time
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  #GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)  # GPIO 23

  
  #GPIO = 23
  # try:
  # if DHT22 > 25
  #print('按下 Ctrl-C 可停止程式')
  # while True:
  # if :
  global pinFAN
  F = int(input('Put FAN ON(1) or OFF(0) :'))
  # if :
  if F == 1:
    GPIO.output(16, 1)
    pinFAN = 1
  else:
    GPIO.output(16, 0)
    pinFAN = 0
  # else:
    # time.sleep(10)

    # GPIO.output(16,False)
    # time.sleep(10)

  # except KeyboardInterrupt:
  # print('關閉程式')


def fansw():
  if pinFAN == 1:
    print('FAN ON !')
  else:
    print('FAN OFF !')
