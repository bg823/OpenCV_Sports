# create 3images, blue/red/green

import numpy as np  # import numpy
import cv2  # import opencv

# initialize with 0.
# create Three-dimensional array is type uint8
# image size 400 * 400 and three colors(channel)
# np.zeroz((line, row, color_channel))
img = np.zeros((400, 400, 3), np.uint8)

# create blue image
img[:, :] = [255, 0, 0]
# writing blue image in main folder
cv2.imwrite('result/blueImage.jpg', img)
# show image on window
cv2.imshow('img1', img)

# create green image
img[:, :] = [0, 255, 0]
# writing blue image in main folder
cv2.imwrite('result/greenImage.jpg', img)
# show image on window
cv2.imshow('img2', img)

# create red image
img[:, :] = [0, 0, 255]
# writing blue image in main folder
cv2.imwrite('result/redImage.jpg', img)
# show image on window
cv2.imshow('img3', img)

while True:
    # push esc kye is exit
    if cv2.waitKey(0) & 0xff == 27:
        # closing all Window
        cv2.destroyAllWindows()
        break
