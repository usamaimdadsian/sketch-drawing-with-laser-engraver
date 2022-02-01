import RPi.GPIO as GPIO
# from RpiMotorLib import RpiMotorLib
from a4988 import A4988Nema
import time


class Motor:
    def __init__(self,dir_pin,step_pin):
        self.motor = A4988Nema(dir_pin, step_pin, (21,21,21), "DRV8825") #Here MS1,MS2,MS3 are all connected to 21 and equal to zero
        self.dir_pin,self.step_pin = (dir_pin,step_pin)

    def move(self,steps,delay=0.05):
        self.clockwise,self.steps = ((steps > 0),abs(steps))

        # GPIO.output(self.en_pin,GPIO.LOW) # pull enable to low to enable motor
        # (True=Clockwise; False=Counter-Clockwise,Step type (Full,Half,1/4,1/8,1/16,1/32),number of steps,step delay [sec],True = print verbose output,# initial delay [sec])
        self.motor.motor_go(self.clockwise,"Full", self.steps, .001, False, delay)

    def cleanup(self):
        GPIO.cleanup() # clear GPIO allocations after run