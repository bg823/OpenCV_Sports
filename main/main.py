"""
Drowing Functions in OpenCV
reference site : https://docs.opencv.org/4.2.0/dc/da5/tutorial_py_drawing_functions.html
"""
import cv2
import numpy as np


# 真っ黒なイメージを作成 width height共に512PX
img = np.zeros((512, 512, 3), np.uint8)

# 白で指定したテキストを描く
# cv2.putText(書き込むイメージ, 書きたいテキスト, テキストの左端, フォント, フォントサイズ, 色, 太さ)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# 画像の表示
cv2.imshow('putText windwow', img)

# 何かしらのキーが押されたら、表示しているwindowを破棄する
cv2.waitKey(0)
cv2.destroyAllWindows()
