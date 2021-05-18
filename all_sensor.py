#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(22, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT,initial=GPIO.LOW)

# BCM=GPIO,BOARD=PIN
#GPIO.setup(18, GPIO.OUT,initial=GPIO.LOW) #pin 12 DHT
#GPIO.setup(23, GPIO.OUT,initial=GPIO.LOW) #pin 16 fan
#GPIO.setup(24, GPIO.OUT,initial=GPIO.LOW) #pin 18 led
# GPIO.setup(25, GPIO.OUT,initial=GPIO.LOW) #pin 22 wat
# GPIO.setup(12, GPIO.OUT,initial=GPIO.LOW) #pin 32
# GPIO.setup(16, GPIO.OUT,initial=GPIO.LOW) #pin 36

# function{}**********

# main{}**********

od = int(input('open the system ? (Open--1 or s_down--0) :'))
import FAN
import LED
import WAT
if od == 1:
  FAN.fan()
  FAN.fansw()
  LED.led()
  LED.ledsw()
  WAT.wat()
  WAT.watsw()
else:
   print('shutdown the system ?')
