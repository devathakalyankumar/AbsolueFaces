import cv2
face_cascade = cv2.CascadeClassifier('./FILE/fface.xml')
cap = cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('./FILE/trainData.yml')
#id=0
font=cv2.FONT_ITALIC
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        print(id,conf)

        #print(val)
        if conf<50:
            id = 'unknown'
            cv2.putText(img, id, (x - 30, y - 30), font, 2, 255)
        else:
            cv2.putText(img, str(id), (x, y - 30), font, 1, 255)
    cv2.imshow('vlo', img)

    if  cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
