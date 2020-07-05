import cv2
import numpy as np

# Different ways are there to detect Edges
img = cv2.imread('dataset/imp.jpg')

image = cv2.resize(img, (410, 240))

# Detecting edges with Sobelx
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Detecting edges withSobely
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Detecting edges with Laplacian function
laplacian = cv2.Laplacian(image, cv2.CV_64F)


# Detecing edges with Canny Function
canny = cv2.Canny(image, 100, 200)

# Detecting edges with mask and bitwise
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red = np.array([30, 150, 50])
upper_red = np.array([255, 255, 180])
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(hsv, hsv, mask=mask)

# Binary Threshold
#Need to tune your threshold value to achieve good results on real world images
_, binary = cv2.threshold(img, 225, 255, cv2.THRESH_BINARY_INV)


cv2.imshow('original_image', img)
cv2.imshow('Binary_thresh', binary)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('laplacian', laplacian)
cv2.imshow('canny Function', canny)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
