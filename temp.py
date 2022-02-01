import time
import numpy as np
from Motor import Motor
from Controller import Controller

if __name__ == '__main__':
    mat = np.zeros((200,200),np.uint8)
    c = Controller(mat,mat)
    # m1 = Motor(17,27) #11,13 
    # m2 = Motor(22,23) #15,16



    while True:
        inp = input(":")
        if inp == "q":
            break


        # m1.move(int(inp))
        # m2.move(int(inp))

        arr = inp.split(",")
        # x,y = (int(arr[0]),int(arr[1]))
        x,y = (100,100)
        c.moveAt(x*10,y*10)
