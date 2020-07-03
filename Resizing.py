import cv2
import numpy as np
import matplotlib.pyplot as plt

# % matplotlib qt
# This is a magic command to display in an external window
image1 = cv2.imread('dataSet/image1.jpg')
image2 = cv2.imread('dataSet/image2.jpg')
cartoon=cv2.imread('dataset/cartoon.jpg')
height, width=cartoon.shape[:2]
# cv2.addWeighted is applied over the image inputs with applied parameters
img1high = cv2.addWeighted(image1, 0.9, image2, 0.1, 0)
img1low = cv2.addWeighted(image1, 0.1, image2, 0.9, 0)
resized2 = cv2.resize(image1,(350,220),interpolation = cv2.INTER_NEAREST)
half_size = cv2.resize(cartoon, (int(width/2), int(height/2)), interpolation= cv2.INTER_CUBIC)
double_size = cv2.resize(cartoon, (int(width*2), int(height*2)), interpolation= cv2.INTER_CUBIC)

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.
M = cv2.getRotationMatrix2D((height / 2, width / 2), 45, 1)
cartoon_wrapped = cv2.warpAffine(cartoon, M, (height,width))

# the window showing output image with the weighted sum
cv2.imshow('original', image1)
cv2.imshow('image 1 hight image1', img1high)
cv2.imshow('Image2 light image', img1low)
cv2.imshow('Resized2 using interpolation', resized2)
cv2.imshow('Original cartoon', cartoon)
cv2.imshow('Half Size', half_size)
cv2.imshow('Double Size', double_size)
cv2.imshow('Cartoon_Wrapped', cartoon_wrapped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Visualizing using MatplotLib
half = cv2.resize(cartoon, (0, 0), fx=0.1, fy=0.1)
bigger = cv2.resize(cartoon, (1050, 1610))

stretch_near = cv2.resize(cartoon, (780, 540),
                          interpolation=cv2.INTER_NEAREST)

Titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [cartoon, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()

# De-allocate any associated memory usage

