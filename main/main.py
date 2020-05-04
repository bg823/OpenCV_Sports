"""
OpenCV Tutorial Video Capture
site : https://docs.opencv.org/4.2.0/dd/d43/tutorial_py_video_display.html
"""
import cv2
import numpy as np


# 真っ黒なイメージを作成 width height共に512PX
img = np.zeros((512, 512, 3), np.uint8)

# 5ピクセルの青いラインを0から511まで描画する
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 画像の表示
cv2.imshow('line windwow', img)

# 何かしらのキーが押されたら、表示しているwindowを破棄する
cv2.waitKey(0)
cv2.destroyAllWindows()
