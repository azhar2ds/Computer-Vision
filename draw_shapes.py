import numpy as np
import matplotlib.pyplot as plt
import cv2

opencv=cv2.imread('dataset/rock3.jpg') #Opencv read image in BGR order

# finding Height & Width
h,w= opencv.shape[:2]


#Drawing shapes

#cv2.line(img,(Pt1,Pt2), color, thickness) where pt1 & 2 are coordinates
line = cv2.line(opencv ,(0,0),(w-1,h-1),(255,0,0), 2)
#cv2.rectangle(img,(Pt1,Pt2),color,thickness) where pt1 & 2 top left and the bottom right coordinates
rectangle=cv2.rectangle(opencv,(115,60),(145,70), (0,0,255),3)
#cv2.circle(img,(Center point coordinates),radius, color, thickness)
circle=cv2.circle(opencv, (130,50),9,(0,255,0),-1) # -1 will fill the circle

cv2.imshow('cv2Readed_image', opencv ) # Displaying in Opencv order
cv2.imshow('line',line)
cv2.imshow('rectangle',rectangle)
cv2.imshow('circle',circle)
cv2.waitKey(0)
cv2.destroyAllWindows()