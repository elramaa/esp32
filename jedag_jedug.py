from machine import Pin
from time import sleep

red = Pin(27, Pin.OUT)
yellow = Pin(26, Pin.OUT)
green = Pin(25, Pin.OUT)

try:
    while True:
        red.on()
        sleep(0.1)
        red.off()
        yellow.on()
        sleep(0.1)
        yellow.off()
        green.on()
        sleep(0.1)
        green.off()
except:
    red.off()
    yellow.off()
    green.off()