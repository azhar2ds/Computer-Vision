import cv2
import pytesseract

original = cv2.imread('dataset/text.jpg')
img = original.copy()  # copying original image

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    R_image = cv2.rectangle(
        img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    cv2.putText(img, b[0], (int(b[1]), h - (int(b[2]))+25),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 1)

cv2.imshow('Original Image', original)
cv2.imshow('Rectangular_Image', R_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(pytesseract.image_to_string(original))
