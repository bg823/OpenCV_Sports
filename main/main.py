# create 3images, blue/red/green

import numpy as np  # import numpy
import cv2  # import opencv

# initialize with 0.
# create Three-dimensional array is type uint8
img1 = np.zeros((400, 400, 3), np.uint8)

# create background black in blue line circle image
# from center 200px, 200px and  50px radius, 1px line
cv2.circle(img1, (200, 200), 50, (255, 0, 0), 1)

# save circle image and show
cv2.imwrite('result/circle1.png', img1)
cv2.imshow('circle1', img1)

# initialize with 0.
# create Three-dimensional array is type uint8
img2 = np.zeros((400, 400, 3), np.uint8)

# create background black in green line circle image
# from center 200px, 200px and  100px radius, 3px line
cv2.circle(img2, (200, 200), 100, (0, 255, 0), 3)

# save circle image and show
cv2.imwrite('result/circle2.png', img2)
cv2.imshow('circle2', img2)

# initialize with 0.
# create Three-dimensional array is type uint8
img3 = np.zeros((400, 400, 3), np.uint8)

# create background black in green line circle image
# from center 200px, 200px and  50px radius, 1px line
cv2.circle(img3, (200, 200), 150, (0, 0, 255), -1)

# save circle image and show
cv2.imwrite('result/circle3.png', img3)
cv2.imshow('circle3', img3)

# end when key is pressed and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()