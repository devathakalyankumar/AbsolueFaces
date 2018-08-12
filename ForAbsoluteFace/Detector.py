import cv2

face_cascade = cv2.CascadeClassifier('./FILE/fface.xml')
cap = cv2.VideoCapture(0)
#print(help(cv2.rectangle))
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
    cv2.imshow('ImageFrame', img)
    if  cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

