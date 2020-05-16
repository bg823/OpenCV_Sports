"""
Mouse as a Paint-Brush in OpenCV
reference site : https://docs.opencv.org/4.2.0/db/d5b/tutorial_py_mouse_handling.html
"""
import cv2
import numpy as np

drowing = False
mode = True
ix, iy = -1, -1


# マウスコールバック関数
def drow_circle(event, x, y, flags, param):
    global ix, iy, drowing, mode

    # print(mode)

    # マウスの左ボタンが押された場合
    if event == cv2.EVENT_LBUTTONDOWN:
        drowing = True
        ix, iy = x, y
    # マウスポインタがウィンドウ上に移動した
    elif event == cv2.EVENT_MOUSEMOVE:
        if drowing == True:
            if mode == True:
                # 四角を描画する
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                # 円を描画する
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    # マウスの左ボタンが離された
    elif event == cv2.EVENT_LBUTTONUP:
        drowing = False
        if mode == True:
            # 四角を描画する
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            # 円を描画する
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


# イメージの作成とwindowの作成、setMouseCallbackにバインド
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
# drow_circleには、自分の行ったマウスの操作・そのXY座標、フラグ、ユーザーオプションのパラメータが入ってくる
cv2.setMouseCallback('img', drow_circle)

while (1):
    cv2.imshow('img', img)
    # Tabが押されたら、modeをFalseに設定
    key = cv2.waitKey(1) & 0xFF
    if key == 9:
        mode = not mode
        # escが押されたら、window破棄
    elif key == 27:
        break

cv2.destroyAllWindows()
