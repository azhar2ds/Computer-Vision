import cv2
import numpy as np

i = cv2.imread('dataset/peter.jpg')

brd=cv2.copyMakeBorder(i, 60,60,60,60, cv2.BORDER_CONSTANT)
brf=cv2.copyMakeBorder(i, 60,60,60,60, cv2.BORDER_REFLECT)
brf101=cv2.copyMakeBorder(i, 60,60,60,60, cv2.BORDER_REFLECT101)
brep=cv2.copyMakeBorder(i, 60,60,60,60, cv2.BORDER_REPLICATE)
brdf=cv2.copyMakeBorder(i, 60,60,60,60, cv2.BORDER_DEFAULT)
stacked_image=np.hstack((brd, brf, brf101, brep, brdf))
cv2.imshow('frame', stacked_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
