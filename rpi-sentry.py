#!/usr/bin/python

##
## Raspberry Pi Home Sentry - RPI script to monitor home
##

## Version 1 - Simple door monitor

## load libraries
import RPi.GPIO as io
import time

print "RPi Home Sentry\n\n"

## set GPIO mode to BCM - allows us to use GPIO number instead of pin number
io.setmode(io.BCM)
io.setwarnings(False)

## set GPIO pins to use
door_pin = 23
led_pin = 17
print("Sentry Activated - Watching: GPIO %d" % door_pin)
print("  Using LED on GPIO %d" % led_pin)

## use the built-in "pull-up" resistor
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input
io.setup(led_pin, io.OUT) # activate LED

## States for door: 0=closed, 1=open, 2=init
door=2
watchcount=0

## infinite loop
while True:
    ## if switch is open
    if (io.input(door_pin)==True and door!=0):
        door=0
        print("Door closed after %d seconds" % watchcount)
        # do some action
	io.output(led_pin,io.LOW)
    ## if switch is closed
    if (io.input(door_pin)==False and door!=1):
        door=1
	watchcount = 0
        print "Door open"
        # do some action
	io.output(led_pin,io.HIGH)
    if (door==1):
	watchcount = watchcount + 1
	print("\rCount: %ds" % watchcount)
    time.sleep(1) # 1 second wait
