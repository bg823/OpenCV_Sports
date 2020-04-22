
import sys # import system
import cv2 # import opencv


img = cv2.imread('/Users/h-nagaoka/Dev/OpenCV_Sports/images/bg823.png')

# if can't read it exit
if img is None:
    sys.exit()


# Draw Hello OpenCV on image
# putText Parameters(img, putText, Lower left Coordinate, Font, font scale, font color, thickness)
cv2.putText(img, 'Hello OpenCV', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (50, 60, 80), 2)

# save image and show
cv2.imwrite('result/hello_opencv.png', img)
cv2.imshow('line', img)

# end when key is pressed and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()