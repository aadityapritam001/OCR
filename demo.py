# from imutils import contours
import numpy as np
# import argparse
# import imutils
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"



# converting it to binary image by Thresholding
# this step is require if you have colored image because if you skip this part 
# then tesseract won't able to detect text correctly and this will give incorrect result
def thresh(image):
#     return cv2.threshold(image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,15)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#dilation
def dilate(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

def blur(img) :
    img_blur = cv2.GaussianBlur(img,(7,7),1) 
    return img_blur


def sharpen(image):
    kernel = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def opening(image):
    kernel = np.ones((1,1),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def canny(image):
    return cv2.Canny(image, 100, 200)

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img



def main():

    image_name=input("Enter the Image path:\t")
    image = cv2.imread(image_name)

    img=get_grayscale(image)
    # img=canny(image)
    img=blur(img)
    # img=dilate(img)
    img=sharpen(img)
    img=erode(img)
    img=dilate(img)

    # display image
    # img=opening(img)
    img=thresh(img)
    img=opening(img)
    img=sharpen(img)
    img=erode(img)
    # img=increase_brightness(img)
    img=blur(img)
    img=sharpen(img)
    # img=255-img
    # cv2.imshow('threshold image',img)
    # Maintain output window until user presses a key
    # cv2.waitKey(0)
    # Destroying present windows on screen
    # cv2.destroyAllWindows()
    cv2.imwrite('./3rd.jpg',img)
    return img