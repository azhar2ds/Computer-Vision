import cv2
import numpy as np

# Reading an image in default mode
image = cv2.imread('dataSet/ge.jpg')
image_with_noise = cv2.imread('dataSet/j_noise.jpg')  # image with Noises
colorimage_withnoise = cv2.imread('dataSet/tajmahal.jpg')

# Creating kernel, As kernels can be created in different ways, But numpy is the easiest one...
kernel = np.ones((5, 5), np.uint8)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  --> RECTANGULAR KERNEL
# kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))  --> ELLIPTICAL KERNEL
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))  --> CROSS SHAPED KERNEL

# Using cv2.erode() method
eroded_image = cv2.erode(image, kernel)
Reflect_image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)
iteration_image = cv2.erode(image, kernel, cv2.BORDER_REFLECT, iterations=1)

# Using cv2.dilate() method
dilate = cv2.dilate(image, kernel, iterations=1)

# Using cv2.morphologyEx() method
morph_open = cv2.morphologyEx(image_with_noise, cv2.MORPH_OPEN, kernel)  # image with some noise
morph_close = cv2.morphologyEx(image_with_noise, cv2.MORPH_CLOSE, kernel)  # image with some noise
morph_gradient = cv2.morphologyEx(image_with_noise, cv2.MORPH_GRADIENT, kernel)
morph_tophat = cv2.morphologyEx(image_with_noise, cv2.MORPH_TOPHAT, kernel)
morph_blackhat = cv2.morphologyEx(image_with_noise, cv2.MORPH_BLACKHAT, kernel)

bilateral = cv2.bilateralFilter(colorimage_withnoise, 15, 75, 75)
# Displaying the image
cv2.imshow('Eroded_image', eroded_image)
cv2.imshow('original image', image)
cv2.imshow('reflect_image', Reflect_image)
cv2.imshow('iteration_image', iteration_image)
cv2.imshow('dilated_image', dilate)
cv2.imshow('Unmorphed_image', image_with_noise)
cv2.imshow('Morphed_OPEN_image', morph_open)
cv2.imshow('Morphed_CLOSE_image', morph_close)
cv2.imshow('Morphed_gra_image', morph_gradient)
cv2.imshow('Morphed_tophat_image', morph_tophat)
cv2.imshow('Morphed_blackhat_image', morph_blackhat)
cv2.imshow('OrigianlColorImage_withNOISE', colorimage_withnoise)
cv2.imshow('colorImage_Withoutnoise', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()