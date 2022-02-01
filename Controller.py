import time
import threading
import numpy as np
from Motor import Motor
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# TODO check how many rotations it takes to cover the whole board
class Controller:
    # XMAX = 1900
    # yMax = 1780
    def __init__(self,scene,board):
        self.mx,self.my = (Motor(17,27),Motor(22,23))
        self.x, self.y = (0,0)


        # GPIO.setup(4, GPIO.OUT)
        # self.p = GPIO.PWM(25, 50)
        # self.p.start(11)

        self.p = 25
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.p, GPIO.OUT)
        GPIO.output(self.p, GPIO.HIGH)

        self.initPos()
        self.z = False

    def moveAt(self,x,y,draw=False,adjacent=False,left=True):
        x,y = (int(x),int(y))
        # TODO write code to move at x,y
        t1 = threading.Thread(target=self.mx.move,args=(x-self.x,0.001))
        t2 = threading.Thread(target=self.my.move,args=(y-self.y,0.001))
        # self.mx.move(x-self.x)
        # self.my.move(y-self.y)
        t1.start()
        t2.start()

        t1.join()
        t2.join()

        self.x, self.y = (x,y)
        if draw and (not self.z): self.pencil(True)
        if (not adjacent) and self.z: self.pencil(False)

    def currentPos(self):
        return (int(self.x/10),int(self.y/10))
            
    def pencil(self,draw):
        if draw:
            # TODO Write code to move servo for drawing 
            # self.p.ChangeDutyCycle(11)
            GPIO.output(self.p,GPIO.HIGH)
            self.z = True
        else:
            # TODO code to move pencil to initial position
            # self.p.ChangeDutyCycle(5)
            GPIO.output(self.p,GPIO.LOW)
            self.z = False
        time.sleep(0.5)
    
    def initPos(self):
        self.pencil(False)
        # TODO try to move motors mx and my to right and bottom as much as possible
        self.moveAt(0,0,draw=False)
        


# motors can be move in steps