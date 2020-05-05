"""
Drowing Functions in OpenCV
reference site : https://docs.opencv.org/4.2.0/dc/da5/tutorial_py_drawing_functions.html
"""
import cv2
import numpy as np


# 真っ黒なイメージを作成 width height共に512PX
img = np.zeros((512, 512, 3), np.uint8)

# polylineを描画するための配列を作成
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))

# 黄色の多角線を描く
# cv2.polylines(書き込むイメージ, 多角線の配列, 多角線が閉じているかTrue False, 色, エッジの太さ)
cv2.polylines(img, [pts], True, (0, 255, 255))

# 画像の表示
cv2.imshow('polylines windwow', img)

# 何かしらのキーが押されたら、表示しているwindowを破棄する
cv2.waitKey(0)
cv2.destroyAllWindows()
