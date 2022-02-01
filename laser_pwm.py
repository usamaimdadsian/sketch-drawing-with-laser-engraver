import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(22,GPIO.OUT)

pin = GPIO.PWM(22,500)

pin.start(0)

try:
   while True:	
    br = int(input("Brightness (max 100)"))
    if br > 100:
        br = 100
    if br<0:
        br = 0
    pin.ChangeDutyCycle(br)
except KeyboardInterrupt:
    pass

pin.ChangeDutyCycle(0)

pin.stop()


GPIO.cleanup()