import cv2
import numpy as np
import matplotlib.pyplot as plt

# % matplotlib qt
# This is a magic command to display in an external window
image1 = cv2.imread('dataSet/image1.jpg')
image2 = cv2.imread('dataSet/image2.jpg')
star = cv2.imread('dataSet/star.jpg')
d = cv2.imread('dataSet/d.jpg')
# cv2.addWeighted is applied over the
# image inputs with applied parameters
img1high = cv2.addWeighted(image1, 0.9, image2, 0.1, 0)
img1low = cv2.addWeighted(image1, 0.1, image2, 0.9, 0)
star_image = cv2.subtract(star, d)
# the window showing output image
# with the weighted sum
cv2.imshow('original', image1)
cv2.imshow('image 1 hight image1', img1high)
cv2.imshow('image2 light image', img1low)
cv2.imshow('subtracted d sign from star', star_image)

# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()