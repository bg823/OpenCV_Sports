"""
OpenCV Tutorial Video Capture
site : https://docs.opencv.org/4.2.0/dd/d43/tutorial_py_video_display.html
"""
import cv2

# ビデオキャプチャ生成、引数はカメラデバイスの番号
# 自分がキャプチャしたい、ビデオ番号を指定
# PCのデフォルトを使う場合は、1 or 0 or -1 その他の可能性もあり
cap = cv2.VideoCapture(0)

# cap.isOpen()でキャプチャが生成されているか確認することができる
# return パラメーターは　True or False
while (cap.isOpened()):
    # retには、読み込めているかどうかのbool値、frameには1フレームが入ってくる
    ret, frame = cap.read()

    # retがTrueじゃなければ、break
    if not ret:
        break

    # カラーフレームをグレーフレームに変換(RGB->GRAY)
    # cvtColor(input_img, flg)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # window sizeをdefaultから、X=320, Y=240に変更
    gray = cv2.resize(gray, dsize=(320, 240))
    # グレー変換した、フレームをcaputreという名前のWindowで表示
    cv2.imshow('capture', gray)

    # escキーが押された場合、ブレークしてwhileを抜ける
    # 0にすると、キーを受け付けるまで、待機してしまうため、フレームが更新されない
    # そのため、適切な数値を振る必要がある
    # 今回の場合、待機は1msecになる
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ビデオファイルまたは、キャプチャデバイスを閉じる
cap.release()

# 表示している画面を破棄
cv2.destroyAllWindows()
