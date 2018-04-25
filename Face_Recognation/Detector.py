import numpy as np
import cv2
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer//trainingData.yml')
font = cv2.FONT_HERSHEY_SIMPLEX
Id =0 
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        Id , conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(Id==1):
            Id= "siddhant" 
        else:
            Id= "hi"
        cv2.putText((img), str(Id), (x, y + h), font, 2, 255);
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
