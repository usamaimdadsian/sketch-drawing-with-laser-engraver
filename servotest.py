import RPi.GPIO as GPIO
import time

servoPIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(11) # Initialization
while True:
  inp = input(":")
  if inp == "q":
    break
  p.ChangeDutyCycle(float(inp))
  time.sleep(0.5)

p.stop()
GPIO.cleanup()