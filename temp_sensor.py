from machine import Pin
from time import sleep
import dht 

# sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(25))

try:
    while True:
      try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print(f'Temperature {temp:3.1f} C')
        print(f'Humidity {hum:3.1f} %%')
      except OSError as e:
        print('Failed to read sensor.')
except:
    print('\nProgram exit with code 0')