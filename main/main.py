
import sys # import system
import cv2 # import opencv


img = cv2.imread('/Users/h-nagaoka/Dev/OpenCV_Sports/images/bg823.png')

# if can't read it exit
if img is None:
    sys.exit()


# writing circle on image
# color is green and skyblue? and yellow
cv2.circle(img, (50, 50), 40, (0, 255, 0), 2)
cv2.circle(img, (150, 150), 80, (255, 255, 0), 6)
cv2.circle(img, (200, 200), 50, (0, 255, 255), -1)

# save image and show
cv2.imwrite('result/line.png', img)
cv2.imshow('line', img)

# end when key is pressed and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()