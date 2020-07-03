# organizing imports
import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
bnc = cv2.imread('dataset/bnc.jpg')
circle = cv2.imread('dataset/circle.jpg')

cv2.imshow('Original circle', circle)

# cv2.bitwise_and is applied over the
# image inputs with applied parameters
bitwise_AND_image = cv2.bitwise_and(bnc, circle)
bitwise_OR_image = cv2.bitwise_or(bnc, circle)
bitwise_XOR_image = cv2.bitwise_xor(bnc, circle)
bitwise_NOT_image = cv2.bitwise_not(bnc, circle)


# the window showing output image
# with the Bitwise AND operation
# on the input images
cv2.imshow('original BNC image', bnc)
cv2.imshow('Bitwise And Image', bitwise_AND_image)
cv2.imshow('Bitwise OR Image', bitwise_OR_image)
cv2.imshow('Bitwise XOR Image', bitwise_XOR_image)
cv2.imshow('Bitwise NOT Image', bitwise_NOT_image)

# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()