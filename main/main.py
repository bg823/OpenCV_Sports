"""
Drowing Functions in OpenCV
reference site : https://docs.opencv.org/4.2.0/dc/da5/tutorial_py_drawing_functions.html
"""
import cv2
import numpy as np


# 真っ黒なイメージを作成 width height共に512PX
img = np.zeros((512, 512, 3), np.uint8)

# 青の楕円を描く
# cv2.ellipse(書き込むイメージ,　楕円の中心, 幅, 楕円回転角度, 楕円弧の開始角度, 楕円弧の終了角度, 色, 太さ)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

# 画像の表示
cv2.imshow('ellipse windwow', img)

# 何かしらのキーが押されたら、表示しているwindowを破棄する
cv2.waitKey(0)
cv2.destroyAllWindows()
