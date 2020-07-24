import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('dataset/shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
corners = cv2.goodFeaturesToTrack(thresh, 25, 0.2, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, 255, -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
