import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('dataset/9img.jpg', 0)

# find frequency of pixels in range 0-255
# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# histr = cv2.calcHist([img],[0],mask=None, histSize=[256], ranges=[0,256])
histr = cv2.calcHist(img, channels=[0], mask=None, histSize=[
                     256], ranges=[0, 256])
# histr=plt.hist(img.ravel(), channels=[0], mask=None, bins=(256), range=(0,256))
#histr = plt.hist(img.ravel(), 256, [0, 256])


# show the plotting graph of an image
plt.plot(histr)
plt.show()
cv2.imshow('grayImage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
images : it is the source image of type uint8 or float32 represented as “[img]”.
channels : it is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and
color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
mask : mask image. To find histogram of full image, it is given as “None”.
histSize : this represents our BIN count. For full scale, we pass [256].
ranges : this is our RANGE. Normally, it is [0,256].

'''
