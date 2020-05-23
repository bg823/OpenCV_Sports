"""
Trackbar as the Color Palette
reference site : https://docs.opencv.org/4.2.0/d9/dc8/tutorial_py_trackbar.html
result url : https://gyazo.com/8c3f57edd605dc18beaf683b778aa46b
"""
import cv2
import numpy as np


# 何もしないコールバック関数
def nothing(x):
    pass


# X = 512 Y = 300の黒いWindowを作成
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# 色を変えることができる、トラックバーを作成する
# トラックバー名, windowの名前, スライダーの初めの位置, スライダーのMAX値, onChange
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# 関数のON/OFFスイッチを作成
# 0 = 色は変化しない, 1 = 色の変化をさせる
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # どの位置にトラックバーがあるか取得する
    # # トラックバーの名前, Windowの名前
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    # switchが0の場合は、色を変化させない.
    # 0出なかった場合は、r/g/bの現在の値をimg配列に代入する
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

# 全てWindowを破棄する
cv2.destroyAllWindows()
