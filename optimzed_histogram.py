import numpy as np
import cv2
from matplotlib import pyplot as plt

# OpenCV function is more faster than (around 40X) than np.histogram().
# So stick with OpenCV function.
img = cv2.imread('dataset/messi.jpg', 0)

# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#hist,bins = np.histogram(img.ravel(),256,[0,256])
# hist = np.bincount(img.ravel(),minlength=256) XX "10 TIMES FASTER"
# plt.hist(img.ravel(),256,[0,256])(MATPLOTLIB)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cv2.imshow('final', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
'''
