import cv2
import pytesseract

original = cv2.imread('dataset/text.jpg')
img = original.copy()  # copying original image

h, w, c = img.shape  # or we can say h, w, _ = img.shape
# it return the boxes coordinate edges as string
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    # x, y, width, height = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    R_image = cv2.rectangle(
        img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)


cv2.imshow('Original Image', original)
cv2.imshow('Rectangular_Image', R_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Passing original image to print the text of an image
print(pytesseract.image_to_string(original))
