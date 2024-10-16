import cv2
import numpy as np

img1 = cv2.imread('image.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('image2.jpg',cv2.IMREAD_COLOR)

#add = img1 + img2
#add = cv2.add(img1,img2)
add = cv2.addWeighted(img1,0.4,img2,0.6,0)

cv2.imshow('image',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
