import cv2
import matplotlib.pyplot as plt


image = cv2.imread('dataset/dark.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalize_hist = cv2.equalizeHist(gray)
cv2.imshow('original', image)
cv2.imshow('Equalize_histogram', equalize_hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

The intuition behind this process is that histograms with large peaks 
correspond to images with low contrast where the background and the 
foreground are both dark or both light. Hence histogram equalization 
stretches the peak across the whole range of values leading to an 
improvement in the global contrast of an image.

'''