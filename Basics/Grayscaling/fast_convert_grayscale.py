import cv2
input = cv2.imread("./Desktop/OpenCV/Basics/hand.jpg",0)
cv2.imshow("Grayscale image",input)
cv2.waitKey()
cv2.destroyAllWindows()
