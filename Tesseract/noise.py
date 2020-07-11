from PIL import Image
import pytesseract

import cv2

Noisy_image = cv2.imread('dataset/Noisy_tesseract.png', 0)
saldnpeper_image = cv2.imread('dataset/salt&pepper.png', 0)

# Defining function to pass threshold on both images


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


nframe = thresholding(Noisy_image)
snpframe = thresholding(saldnpeper_image)

cv2.imshow('Noisy_frame', nframe)
cv2.imshow('salt&peper_image', snpframe)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Tesseract will work fine with Noisy Image
# But if image have salt and peper noise then its hard for tesseract
print('Noisy Image:', pytesseract.image_to_string(nframe), '\n')
print('Salt and peper Image:\n', pytesseract.image_to_string(snpframe))
