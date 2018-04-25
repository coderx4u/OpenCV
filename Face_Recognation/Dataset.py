import cv2
import numpy as np
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
id = raw_input("Enter User Id:")
sn=0;
while True:
    ret , img = cam.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        sn = sn+1;
        cv2.imwrite("dataset/User."+str(id)+"."+str(sn)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0) ,2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sn>20):
        break;
cam.release();
cv2.destroyAllWindows();

