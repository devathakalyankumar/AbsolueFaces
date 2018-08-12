
import cv2

face_cascade = cv2.CascadeClassifier('./FILE/fface.xml')
cap = cv2.VideoCapture(0)
id=input("enter user id")

sample=0
val=None
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        val=cv2.imwrite("./dataset/user." + id + "." + str(sample) + ".jpg", gray[y:y + h, x:x + w])
        sample += 1
        cv2.waitKey(100)

    cv2.imshow('vlo', img)
    if sample >100:
        break

cap.release()
cv2.destroyAllWindows()
