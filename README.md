RPi-HomeSentry
==============

This is a simple Raspberry Pi python script for monitoring the state of an external switch using the GPIO pins on the Pi.  The script detects open and closed states.  For open states, it will count the number of seconds.  This can be used to do a countdown alert or notifier if desired.  I created this to watch my garage door and notify when it is open (see http://www.jasonacox.com/wordpress/archives/355 on how I set up the microswitch).

## Background

See http://www.jasonacox.com/wordpress/archives/355

## Usage

* Attach microswitch to the Raspberry Pi GPIO pin 23 and GND, and the LED to GPIO pin 17 and GND (w/resistor)
* Use `sudo rpi-sentry.py` to run the sentry
* Stop the sentry using ^C

## Example Output

'''
pi@raspberry:~ $ sudo ./rpi-sentry.py
RPi Home Sentry

Sentry Activated - Watching: GPIO 23
  Using LED on GPIO 17
Door closed after 0 seconds
Door open
Count: 1s
Count: 2s
Count: 3s
Count: 4s
Count: 5s
Door closed after 5 seconds
'''