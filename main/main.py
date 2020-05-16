"""
Mouse as a Paint-Brush in OpenCV
reference site : https://docs.opencv.org/4.2.0/db/d5b/tutorial_py_mouse_handling.html
"""
import cv2
import numpy as np


# マウスコールバック関数
def drow_circle(event, x, y, flags, param):
    # マウスの左ボタンがダブルクリックされたら、XY座標にクリックした座標を当てて塗り潰した円を描く
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# イメージの作成とwindowの作成、setMouseCallbackにバインド
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
# drow_circleには、自分の行ったマウスの操作・そのXY座標、フラグ、ユーザーオプションのパラメータが入ってくる
cv2.setMouseCallback('img', drow_circle)

while (1):
    cv2.imshow('img', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
