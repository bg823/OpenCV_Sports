"""
Drowing Functions in OpenCV
reference site : https://docs.opencv.org/4.2.0/dc/da5/tutorial_py_drawing_functions.html
"""
import cv2
import numpy as np


# 真っ黒なイメージを作成 width height共に512PX
img = np.zeros((512, 512, 3), np.uint8)

# 緑色の矩形(長方形)を3PXで描く
# cv2.rectangle(書き込むイメージ, 矩形の頂点, 矩形の頂点の反対側の頂点, 色, 太さ(厚み))
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 画像の表示
cv2.imshow('rectangle windwow', img)

# 何かしらのキーが押されたら、表示しているwindowを破棄する
cv2.waitKey(0)
cv2.destroyAllWindows()
