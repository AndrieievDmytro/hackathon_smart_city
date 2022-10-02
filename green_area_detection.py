import cv2  as cv
import numpy as np 
import os
import csv
from scipy.stats import pearsonr

path = '.'
files = os.listdir(path)
f = open('data.csv', 'w')
writer = csv.writer(f)
for i in files:   
    img = cv.imread(path +'/' + i)
    # low_green = np.array([36,25,25])
    # high_green = np.array([86, 255,255]) 
    low_green = np.array([27,25,25])
    high_green = np.array([120, 255,255]) 
    kernel = np.ones((13, 13), np.uint8)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, low_green, high_green)
    mask_without_noise = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel) 
    mask_close = cv.morphologyEx(mask_without_noise, cv.MORPH_CLOSE, kernel)

    result = cv.bitwise_and(img, img, mask=mask_close) 
    ratio_green = cv.countNonZero(mask)/(img.size)
    name = os.path.splitext(i) 
    data = [i[0] ,"%.2f" %(ratio_green*100)]
    writer.writerow(data)

    print("%.2f" %(ratio_green*100))
    
    cv.imshow('img', img) 
    cv.imshow('result', result) 
    cv.waitKey(0) 

    cv.destroyAllWindows()

f.close

