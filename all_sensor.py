#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import FAN
import LED
import WAT
#BCM=GPIO,BOARD=PIN
GPIO.setwarnings(False)
# GPIO.setup(18, GPIO.OUT,initial=GPIO.LOW) #pin 12 
# GPIO.setup(23, GPIO.OUT,initial=GPIO.LOW) #pin 16 fan
# GPIO.setup(24, GPIO.OUT,initial=GPIO.LOW) #pin 18 led
# GPIO.setup(25, GPIO.OUT,initial=GPIO.LOW) #pin 22 wat
# GPIO.setup(12, GPIO.OUT,initial=GPIO.LOW) #pin 32 
# GPIO.setup(16, GPIO.OUT,initial=GPIO.LOW) #pin 36

#function{}**********

#main{}**********

while True:

        FAN.fan()
        LED.led()
        WAT.wat()
