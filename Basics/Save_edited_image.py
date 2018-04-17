#Sving image we edited
import cv2
input = cv2.imread("./Desktop/OpenCV/Basics/hand.jpg")
cv2.imwrite("Output.jpg",input)
cv2.imwrite("Output.png",input)
