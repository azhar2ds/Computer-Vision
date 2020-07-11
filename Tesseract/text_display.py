import cv2
import pytesseract


# we have to install pytesseract.exe file and give the location of that file
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread('dataset/text.jpg')


print(pytesseract.image_to_string(img))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
