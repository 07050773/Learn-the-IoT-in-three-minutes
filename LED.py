#!/usr/bin/env python3
pinLED = 0


def led():

  global pinLED

  import time
  import RPi.GPIO as GPIO
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  #GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)  # GPIO 23

  # GPIO = 23
  # try:
  # if DHT22 > 25
  # print('按下 Ctrl-C 可停止程式')
  # while True:
  L = int(input('Put LED ON(1) or OFF(0) :'))
  # if :
  if L == 1:
    GPIO.output(18, True)
    pinLED = 1
  else:
    GPIO.output(18, False)
    pinLED = 0

  # else:

  # time.sleep(10)
  # except KeyboardInterrupt:
  # print('關閉程式')


def ledsw():
  if pinLED == 1:
    print('LED ON !')
  else:
    print('LED OFF !')


#led()
#ledsw()
