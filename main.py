import cv2
import numpy as np
from Image import Image
from Drawing import Drawing
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
from picamera import PiCamera




if __name__ == '__main__':
    inPin = 8
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(inPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    while True:
        value = GPIO.input(inPin)
        if not value:
            print("Button pressed")
            camera = PiCamera()
            camera.rotation = 180
            camera.start_preview()
            camera.capture('images/t2.png')
            camera.stop_preview()

            img = cv2.imread('images/t2.png')
            img_o = Image(img,'edge')
            img = img_o.rimg
            
            rimg = img.copy()
            rimg[img == 1] = 255
            cv2.imwrite("images/rt2.png",rimg)
            cv2.imshow("newimg", rimg)


            # img = cv2.imread('index.jpeg')
            # img_o = Image(img,'edge')
            # img = img_o.rimg
            # print(np.unique(img))

            #scene = img
            #board = np.zeros_like(scene)
            #d = Drawing(scene,board)
            #d.bestDraw()
            #break

    # img = cv2.imread('test.png',0)
    # img[img > 127] = 150
    # img[img < 127] = 1
    # img[img == 150] = 0

    GPIO.cleanup()