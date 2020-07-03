# organizing imports
import cv2
import numpy as np

img = cv2.imread('dataSet/bookpage.jpg')

# cv2.cvtColor is applied over the image input with applied parameters to convert the image in grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applying different thresholding techniques on the input image all pixels value above 120 will be set to 255
ret, thresh1 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 180, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 180, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 180, 255, cv2.THRESH_TOZERO_INV)
ret, thresh6 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
thresh8 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

 # the window showing output images with the corresponding thresholding techniques applied to the input images
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
cv2.imshow('ThreshOTSU', thresh6)
cv2.imshow('Adaptive Mean', thresh7)
cv2.imshow('Adaptive Gaussain', thresh8)


# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()