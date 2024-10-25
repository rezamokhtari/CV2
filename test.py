import cv2
import numpy as np

img1 = cv2.imread('image2.jpg')
img2 = cv2.imread('image3.jpg')

rows, cols, channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_bg = cv2.bitwise_and(roi,roi,mask = mask)
img_fg = cv2.bitwise_and(img2,img2, mask = mask_inv)

des = cv2.add(img_bg,img_fg)
img1[0:rows,0:cols] = des


#cv2.imshow('mask',mask)
#cv2.imshow('mask_inv',mask_inv)
#cv2.imshow('im1bg',img_bg)
#cv2.imshow('im2fg',img_fg)
#cv2.imshow('im2',img2)
cv2.imshow('im1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()