# Complete project details at https://RandomNerdTutorials.com/micropython-programming-with-esp32-and-esp8266/

from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(25), sda=Pin(26))

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
framebuf = oled.framebuf

r = 1
x = int(oled_width / 2)
y = int(oled_height / 2)

oled.fill(1)
framebuf.ellipse(x, y, r, r, 0)
oled.show()

while True:
    while r < 25:
        sleep(.01)
        r += 1
        oled.fill(1)
        framebuf.ellipse(x, y, r, r, 0, 1)
        oled.show()
    while r > 0:
        sleep(.01)
        r -= 1
        oled.fill(1)
        framebuf.ellipse(x, y, r, r, 0, 1)
        oled.show()