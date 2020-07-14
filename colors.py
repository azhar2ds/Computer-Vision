import numpy as np
import matplotlib.pyplot as plt
import cv2
from matplotlib import colors
#from matplotlib import colors.hsv_to_rgb

#Colors for OPENCV as we have declare order of BRG
orange = (0, 100, 200)
pink = (250, 0, 240)
blue = (255, 0, 0)
yellow = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)

#Colors for matplotlib
orange_mpt = (20, 210, 230)
pink_mpt = (240, 190, 250)
blue_mpt = (170, 255, 255)
yellow_mpt = (40, 255, 255)
white_mpt = (255, 0, 255)
black_mpt = (0,0,0)

#Color for OPENCV
a=(50,50,3)
d=np.uint8
orange = np.full(a, orange, d)
pink = np.full(a, pink, d)
blue = np.full(a, blue, d)
yellow = np.full(a, yellow, d)
white = np.full(a, white, d)
black = np.full(a, black, d)

#Colors for Matplotlib
orange_mpt = np.full((10, 10, 3), orange_mpt, dtype=np.uint8) / 255.0
pink_mpt = np.full((10, 10, 3), pink_mpt, dtype=np.uint8) / 255.0
blue_mpt = np.full((10, 10, 3), blue_mpt, dtype=np.uint8) / 255.0
yellow_mpt = np.full((10, 10, 3), yellow_mpt, dtype=np.uint8) / 255.0
white_mpt = np.full((10, 10, 3), white_mpt, dtype=np.uint8) / 255.0
black_mpt = np.full((10, 10, 3), black_mpt, dtype=np.uint8) / 255.0

plt.subplot(1, 6, 1)
plt.imshow(colors.hsv_to_rgb(orange_mpt))
plt.subplot(1, 6, 2)
plt.imshow(colors.hsv_to_rgb(pink_mpt))
plt.subplot(1, 6, 3)
plt.imshow(colors.hsv_to_rgb(blue_mpt))
plt.subplot(1, 6, 4)
plt.imshow(colors.hsv_to_rgb(yellow_mpt))
plt.subplot(1, 6, 5)
plt.imshow(colors.hsv_to_rgb(white_mpt))
plt.subplot(1, 6, 6)
plt.imshow(colors.hsv_to_rgb(black_mpt))
plt.show()


cv2.imshow('orange', orange)
cv2.imshow('pink', pink)
cv2.imshow('blue', blue)
cv2.imshow('yellow',yellow)
cv2.imshow('black',black)
cv2.imshow('white',white)
cv2.waitKey(0)
cv2.destroyAllWindows()
