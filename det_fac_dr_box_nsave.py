import cv2

# Five steps to detect the faces from a given image!!!

#Reading the faces from given image
image = cv2.imread('C:/Anaconda3/python/Op/dataset/henry.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Creating object for face detection through HAAR-CASCADE XML file
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(gray, 1.9, 10)

#Drawing Box around the face
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

print("Info: Found", len(faces), " Faces!!!!!\nSaved to the D_dataset Folder successfully...")

#Display an Image
cv2.imshow('image', image)
cv2.waitKey(2000)


# Saving an image
cv2.imwrite('D_dataset/henry.jpg', image)
cv2.destroyAllWindows()