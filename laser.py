import RPi.GPIO as GPIO
import time

LaserGPIO = 25 # --> PIN11/GPIO17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LaserGPIO, GPIO.OUT)
    GPIO.output(LaserGPIO, GPIO.LOW)

# def loop():
#     while True:
#           print('Laser=on')
#           GPIO.output(LaserGPIO, GPIO.HIGH) # led on
#           time.sleep(2)
#           print('Laser=off')
#           GPIO.output(LaserGPIO, GPIO.LOW) # led off
#           time.sleep(2)

def destroy():
    GPIO.output(LaserGPIO, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()

try:
    # loop()
    while True:
        time.sleep(1)
        print('Laser=on')
        GPIO.output(LaserGPIO, GPIO.HIGH) # led on
        time.sleep(3)
        print('Laser=off')
        GPIO.output(LaserGPIO, GPIO.LOW) # led off
except KeyboardInterrupt:
    destroy()