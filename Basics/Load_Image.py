import cv2
input = cv2.imread("./Desktop/OpenCV/Basics/hand.jpg")
cv2.imshow("Read Image",input)
#Allows any key to be pressed
cv2.waitKey()
#This closes all open windows
cv2.destroyAllWindows()
