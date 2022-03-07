import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    time.sleep(0.5)
    while GPIO.output(pin, 1):
        GPIO.output(23, 1)
        GPIO.output(24, 1)
        GPIO.output(25, 1)
    GPIO.output(pin, 0)
    time.sleep(0.5)

for i in range(0,10):
    blink(18)


GPIO.cleanup()
print("Program executed")