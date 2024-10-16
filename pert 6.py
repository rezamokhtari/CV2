import cv2
import numpy as np

img = cv2.imread('image.jpg',cv2.IMREAD_COLOR)

part1 = img[100:200,100:200]
img[300:400,300:400] = part1

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
