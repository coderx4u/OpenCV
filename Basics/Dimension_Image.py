import cv2
import numpy as np
input = cv2.imread("./Desktop/OpenCV/Basics/hand.jpg")
# input.shape return tuples with three value. The first value represent height(x-coordinate), second value
# represent width(y-coordinate) and third value represent returns '3L' which are the RGB values of an Image
print input.shape
print "Height of Image is :",int(input.shape[0]),"pixels";
print "Width of Image is :",int(input.shape[1]),"pixels";
