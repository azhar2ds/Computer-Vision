import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import skimage
import glob


file = 'E:/Pending2uploadingihub/Dataset/Apparel_Random_Dataset/*.*'
path = glob.glob(file)
print('Total Number of Images: ',len(path))

#lets see first 4 images
       
ls=[]
for x in path:
    a = cv2.imread(x)
    ls.append(a)
    for i in range(len(ls)):
        plt.subplot(2,2,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.tight_layout()
        plt.imshow(ls[i])