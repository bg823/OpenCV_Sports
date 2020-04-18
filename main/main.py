"""
OpenCV Tutorial Video Capture
site : https://docs.opencv.org/4.2.0/dd/d43/tutorial_py_video_display.html
"""
import cv2

# ビデオキャプチャ生成、引数はカメラデバイスの番号
# 自分がキャプチャしたい、ビデオ番号を指定
# PCのデフォルトを使う場合は、1 or 0 or -1 その他の可能性もあり
cap1 = cv2.VideoCapture(
    '/your file path/fortnite.mp4')
cap2 = cv2.VideoCapture(
    'your file path/fortnite.mp4')

# cap.isOpen()でキャプチャが生成されているか確認することができる
# return パラメーターは　True or False
while (cap1.isOpened() and cap2.isOpened()):
    # retには、読み込めているかどうかのbool値、frameには1フレームが入ってくる
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # retがTrueじゃなければ、break
    if not ret1 and not ret2:
        break

    # カラーフレームをグレーフレームに変換(RGB->GRAY)
    # cvtColor(input_img, flg)
    gray = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    color = frame2

    # window sizeをdefaultから、X=320, Y=240に変更
    gray = cv2.resize(gray, dsize=(320, 240))
    color = cv2.resize(color, dsize=(320, 240))

    # グレー変換した、フレームをcaputreという名前のWindowで表示
    cv2.imshow('capture1', gray)
    cv2.imshow('capture2', color)

    # escキーが押された場合、ブレークしてwhileを抜ける
    # 0にすると、キーを受け付けるまで、待機してしまうため、フレームが更新されない
    # そのため、適切な数値を振る必要がある
    # 今回の場合は、
    if cv2.waitKey(30) & 0xFF == 27:
        break

# ビデオファイルまたは、キャプチャデバイスを閉じる
cap1.release()
cap2.release()

# 表示している画面を破棄
cv2.destroyAllWindows()
