import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)

for i in range(0,10):
    blink(18)
    blink(23)
    blink(24)
    blink(25)

GPIO.cleanup()
print("Program executed")