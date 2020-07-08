import cv2
import numpy as np


img = cv2.imread('dataset/2kids.jpg')

# Rotating Image
height, width = img.shape[:2]
M = cv2.getRotationMatrix2D((height/2, width/2), 45, 1)
res = cv2.warpAffine(img, M, (height, width))

# Moving Image
a = np.float32([[1, 0, 70], [0, 1, 30]])
b = cv2.warpAffine(img, a, (height, width))

# Edge Detection
det = cv2.Canny(img, 200, 60)

cv2.imshow('original', img)
cv2.imshow('resize', res)
cv2.imshow('moved_image', b)
cv2.imshow('det', det)
cv2.waitKey(0)
cv2.destroyAllWindows()
