import cv2
import numpy as np

image = cv2.imread('dataset/friends.jpg')
cv2.imshow('4FriendsIMG', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('dataset/friend4.jpg', 0)
# result of template matching of object over an image
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
sin_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
# increasing the size of bounding rectangle by 50 pixels
bottom_right = (top_left[0]+80, top_left[1]+80)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

cv2.imshow('4th friend found..', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
