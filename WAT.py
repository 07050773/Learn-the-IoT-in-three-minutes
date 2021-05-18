#!/usr/bin/env python3
pinWAT = 0


def wat():
  global pinWAT

  import time
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  #GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)  # GPIO 23

  # GPIO = 23
  # try:
  # if DHT22 > 25
  # print('按下 Ctrl-C 可停止程式')
  # while True:
  # if :

  W = int(input('Put WAT ON(1) or OFF(0) :'))
  if W == 1:
    GPIO.output(22, True)
    pinWAT = 1
  else:
    GPIO.output(22, False)
    pinWAT = 0
  # else:
    # except KeyboardInterrupt:
    # print('關閉程式')


def watsw():
  if pinWAT == 1:
    print('WAT ON !')
  else:
    print('WAT OFF !')
