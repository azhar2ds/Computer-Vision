import cv2
import matplotlib.pyplot as plt
image = cv2.imread('dataset/image1.jpg')
###############
# Histogram Equalization
channels = cv2.split(image)
eq_channels = []
for ch, color in zip(channels, ['B', 'G', 'R']):
    eq_channels.append(cv2.equalizeHist(ch))
eq_image = cv2.merge(eq_channels)
cv2.imshow("Original", image)
cv2.imshow("Equalized Image", eq_image)
cv2.waitKey()
cv2.destroyAllWindows()
############
# Plot histogram for equalized image
# show Histogram

channels = ('b', 'g', 'r')
for i, color in enumerate(channels):
    histogram = cv2.calcHist([eq_image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
    plt.xlim([0, 256])
plt.show()

# we now separate the colorsAn alternative is to first convert
# the image to the HSV color space and then apply the histogram
# equalization only on the lightness or value channel by leaving the
# hue and the saturation of the image unchanged and plot each in the Histogram

H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
eq_V = cv2.equalizeHist(V)
eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2RGB)
plt.imshow(eq_image)
plt.show()


clahe_img=cv2.imread('dataset/darkroom.jpg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
c = clahe.apply(clahe_img)
cv2.imshow('Original ClAHE image',clahe_img)
cv2.imshow('c',c)
cv2.waitKey(0)
cv2.destroyAllWindows()