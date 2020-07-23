import cv2
import numpy as np


img = cv2.imread('dataset/fruits.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst2 = dst.copy()

# result is dilated for marking the corners, not important
dst3 = cv2.dilate(dst2, None)

print(type(dst3))
print(dst3.shape)
hist = cv2.calcHist([dst3], [0], None, [256], [0, 256])

# Threshold for an optimal value, it may vary depending on the image.
img[dst3 > 0.45*dst3.max()] = [0, 0, 255]


cv2.imshow('final', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
