#import OpenCV
import numpy as np
import cv2

img = cv2.imread('images/bg823.png', 0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()
        break