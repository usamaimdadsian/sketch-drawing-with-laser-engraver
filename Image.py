import cv2

class Image:
    def __init__(self, img, category):
        img_y, img_x = img.shape[:2]
        img = cv2.resize(img, (0,0), fx=400/img_x, fy=356/img_y, interpolation = cv2.INTER_AREA)

        if category == "edge":
            self.edgeImage(img)
        elif category == "sketch":
            self.sketchImage(img)
        else:
            self.testImage()

    def edgeImage(self,img):
        # Convert to black and white
        gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        (thresh, bwimg) = cv2.threshold(gimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        self.bwimg = bwimg
        self.gimg = gimg
        # thresh = 127
        # bwimg= cv2.threshold(gimg, thresh, 255, cv2.THRESH_BINARY)[1]


        # Edge Detection
        imgBlurredColour = cv2.GaussianBlur(img, (7,7),0) #blurs to soften edges, really sure how effetive this is yet
        imgBlurredBlackWhite = cv2.GaussianBlur(self.bwimg, (7,7),0)

        imgOutlinedColour = cv2.Canny(imgBlurredColour, 100, 200) #for colour 
        #processes and outputs an image, 100 200 is the ratio for acceptable edge gradation 
        imgOutlinedBlackWhite = cv2.Canny(imgBlurredBlackWhite, 100, 200) #for black and white
        imgOutlinedGrayscale = cv2.Canny(self.gimg, 100, 200)
        #so that we can merge all three together to get better acuracy of the image

        imgOutlinedTemp = cv2.addWeighted(imgOutlinedBlackWhite,1,imgOutlinedColour,1,0) #merges two photos together
        img = cv2.addWeighted(imgOutlinedTemp,1,imgOutlinedGrayscale,1,0)#merges a third to it
        img[img>0] = 1
        # imgOutlined = cv2.bitwise_not(imgOutlined)
        self.rimg = img


    def sketchImage(self,img):
        self.gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        igimg = 255 - gimg
        blurred_img = cv2.GaussianBlur(igimg, (21,21),0)
        inv_blurred_img = 255 - blurred_img
        pencil_sketch_img = cv2.divide(gimg,inv_blurred_img, scale = 256.0)
        pencil_sketch_img = cv2.bitwise_not(pencil_sketch_img)
        pencil_sketch_img[pencil_sketch_img>127] = 255
        img = pencil_sketch_img
        img = cv2.medianBlur(img,11)
        img[img > 127] =1
        self.rimg = img

    def testImage(self,img):
        import numpy as np
        img = np.zeros((200,200),np.uint8)
        img[25:75,10:190] = 255
        img[100:160,10:190] = 255
        img = cv2.resize(img,(0,0), fx=178/200, fy=190/200, interpolation = cv2.INTER_AREA)
        img[img>0] = 1
        self.rimg = img