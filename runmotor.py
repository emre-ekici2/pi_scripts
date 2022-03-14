import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

control_pins = [7, 11, 13, 15]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]


for i in range(2048):
    for halfstep in halfstep_seq[::-1]:
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep[pin])
        time.sleep(0.001)

GPIO.cleanup()