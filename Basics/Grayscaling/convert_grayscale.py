#Grayscaling is the process of converting a full colored images into shades of grey (Black & White)
import cv2
input = cv2.imread("./Desktop/OpenCV/Basics/hand.jpg")
cv2.imshow("colored image",input)
cv2.waitKey()
#cvtColor to convert mage to Grayscale
greyimage = cv2.cvtColor(input , cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image",greyimage)
cv2.waitKey()
cv2.destroyAllWindows()
