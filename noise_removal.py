import cv2
import numpy as np

color_noise = cv2.imread('dataset/tajmahal.jpg')
gray_noise = cv2.imread('dataset/noisy.jpg')

# for gray image noise removal
gus = cv2.GaussianBlur(gray_noise, (5, 5), 0)
medianblur = cv2.medianBlur(gray_noise, 5)

# for color image noise removal
color_noi_rem = cv2.bilateralFilter(color_noise, 15, 75, 75)

cv2.imshow('org_gry', gray_noise)
cv2.imshow('org_color', color_noise)
cv2.imshow('gussian', gus)
cv2.imshow('medianblur', medianblur)
cv2.imshow('color_noi_rem', color_noi_rem)
cv2.waitKey(0)
cv2.destroyAllWindows()
