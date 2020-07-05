import cv2

img=cv2.imread('dataSet/2kids.jpg')
img2=cv2.imread('dataSet/j_noise.jpg')
img3=cv2.imread(('dataSet/fruits.jpg'))
img4=cv2.imread('dataSet/imp.jpg',0)
img5=cv2.imread('dataSet/tajmahal.jpg')

# Equalizing Histogram function
hist = cv2.equalizeHist(img4)
cv2.imshow('original Hist', img4 )
cv2.imshow('equalizeHist', hist)
cv2.waitKey(0)


#Blurr a surronding
img1=cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REPLICATE)
cv2.imshow('originalImage', img)
cv2.imshow('i', img1)
cv2.waitKey(0)

# reducing noise using median blur for binary image
median = cv2.medianBlur(img2, 5)
cv2.imshow('original image2', img2)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

# High End resolution BLUR using Gaussian Blur
guassian_blur=cv2.GaussianBlur(img3, (15,15), 0)
cv2.imshow('Original', img3)
cv2.imshow('guassian_blur', guassian_blur)
cv2.waitKey(0)

# Bilateral Blur
bilateral = cv2.bilateralFilter(img3, 9, 475, 475)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)

# Reducin noise for a color Image using BilateralFilter()
biColor = cv2.bilateralFilter(img5, 20, 90,80)
cv2.imshow('originalImage_withNoise', img5)
cv2.imshow('colornoise_reduced', biColor)
cv2.waitKey(0)
cv2.destroyAllWindows()