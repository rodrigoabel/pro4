#!/usr/bin/env python

# This program will detect specific IP address on the network and 
# Enable an LED if it is detected 

import RPi.GPIO as GPIO, time, os
from subprocess import call


SLEEP_TIME = 1

host1 = "192.168.1.41" # my iPhone
host2 = "192.168.1.78" # wife's iphone
host3 = "192.168.1.186" # an iPad

GPIO.setmode(GPIO.BCM)
GREEN_LED = 24
RED_LED = 23
BLUE_LED = 18


GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

def detect_IP(ip_add, color_led):
 ping_command = "ping -c 1 %s > /dev/null 2>&1" % ip_add


 if call(ping_command, shell=True) > 0:
  GPIO.output(color_led, False)
  print("no encontrado :(")

 else:
  GPIO.output(color_led, True)
  print("encontrado !!!!! :D")
 
try:

    while True:
        #detect_IP(host1, GREEN_LED)
        detect_IP(host2, RED_LED)
        #detect_IP(host3, BLUE_LED)
        time.sleep(SLEEP_TIME)  
        
except KeyboardInterrupt:
      GPIO.cleanup()
        
