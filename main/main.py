
import sys # import system
import cv2 # import opencv


img = cv2.imread('/Users/h-nagaoka/Dev/OpenCV_Sports/images/bg823.png')

# if can't read it exit
if img is None:
    sys.exit()

# create 3 line colors on read image
# writing line is Coordinate X50Y50-X200-Y50 and X50Y100-X200Y100 and X100Y150-X200Y150
# thickness 5 and 10px
cv2.line(img, (50, 50), (200, 50), (255, 0, 0))
cv2.line(img, (50, 100), (200, 100), (0, 255, 0), 5)
cv2.line(img, (100, 150), (200, 150), (0, 0, 255), 10)

# save image and show
cv2.imwrite('result/line.png', img)
cv2.imshow('line', img)

# end when key is pressed and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()