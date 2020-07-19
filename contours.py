import cv2
import numpy as np
import matplotlib.pyplot as plt

# contours are the continuous lines or curves that bound
# or cover the full boundary of an object in an image

image = cv2.imread('dataSet/shapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny image is good for text capturing
canny = cv2.Canny(gray, 30, 200)

# Detecting images in binary format
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

# Finding contours,
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Total Number of contours:', len(contours))
# It counts total number of full boundaries of an object

print(hierarchy)
# draw all contours
contoured = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 2)
# Its better to copy your original image inorder to keep your original unchaged
# use -1 to draw all the contours,  4th options for colors,  5th options for thinkness


plt.imshow(contoured)
plt.show()

cv2.imshow('original', image)
cv2.imshow('binary', binary)
cv2.imshow('Canny Image', canny)
cv2.imshow('contour detected', contoured)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To achieve good results on different and real world images,
# you need to tune your threshold value or perform edge detection