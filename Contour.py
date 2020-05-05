import numpy as np
from PIL import Image,ImageChops
import cv2
import matplotlib.pyplot as plt

def after():#take picture after every 5 min and run contour model
    im = cv2.imread(r'C:\Users\admin\Desktop\OSA.jpg')
    gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Gray Scale Image",gray)
    cv2.waitKey(0) 
    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    edged = cv2.Canny(gray, 30, 200) 
    contours, hierarchy = cv2.findContours(edged, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    cv2.imshow('Canny Edges After Contouring', edged) 
    cv2.drawContours(im, contours, -1, (0, 255, 0), 5)
    cv2.waitKey(0) 
    cv2.imshow('Contours', im)
    cv2.waitKey(0) 
    sum = 0
    for c in contours:
        area = cv2.contourArea(c)
        sum = area+sum
    print("Area of contour (Picture Taken After Some time) : ",sum)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    return sum

def difference(s1,s2):
    img1 = Image.open(r'C:\Users\admin\Desktop\OSA.jpg')
    img2 = Image.open(r'C:\Users\admin\Desktop\OSA before.jpg')
    diff = ImageChops.difference(img1,img2)
    #if after pictures contour area value is less than before pictures contour value
    #invoke alert function which sends the image of products that are to be replenished from stock
    if (diff.getbbox()):#and (s2<=(s1*0.5))):#send alert to admin to replenish the stock
        diff.save(r'C:\Users\admin\Desktop\diff.jpg')
        im = cv2.imread(r'C:\Users\admin\Desktop\diff.jpg')
        cv2.imshow('Inventories to be Replenished', im) 

    
def before():# take picture with full products in shelf
    im = cv2.imread(r'C:\Users\admin\Desktop\OSA before.jpg')
    gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Gray Scale Image",gray)
    cv2.waitKey(0) 
    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    edged = cv2.Canny(gray, 30, 200) 
    contours, hierarchy = cv2.findContours(edged, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    cv2.imshow('Canny Edges After Contouring', edged)
    cv2.waitKey(0) 
    cv2.drawContours(im, contours, -1, (0, 255, 0), 5)
    sum = 0
    for c in contours:
        area = cv2.contourArea(c)
        sum = area+sum
    print("Area of contour (Initial Picture): ",sum)
    cv2.imshow('Contours', im)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    return sum
    
s1 = before()
s2 = after()
difference(s1,s2)
