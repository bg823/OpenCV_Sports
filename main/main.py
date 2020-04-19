"""
OpenCV Tutorial Video Capture
site : https://docs.opencv.org/4.2.0/dd/d43/tutorial_py_video_display.html
"""
import cv2

# ビデオキャプチャ生成、引数はカメラデバイスの番号
# 自分がキャプチャしたい、ビデオ番号を指定
# PCのデフォルトを使う場合は、1 or 0 or -1 その他の可能性もあり
cap1 = cv2.VideoCapture('/your file path/fortnite.mp4')

#出力コーデック名指定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#　int変換して、幅の取得
# height = int(cap1.get(3))

# int変換して、高さ取得
# width = int(cap1.get(4))

# 書き込み設定　VideoWriter(保存するファイル名,設定した拡張子, 出力するフレームレート, 保存するフレームサイズ)
# 320, 240のところは、上のheight, widthと指定してもOKです.その際はしたのcv2.resizeを削除してください.
out = cv2.VideoWriter('movie/save_movie.mp4', fourcc, 30.0, (320, 240))

# cap.isOpen()でキャプチャが生成されているか確認することができる
# return パラメーターは　True or False
while (cap1.isOpened()):
    # retには、読み込めているかどうかのbool値、frameには1フレームが入ってくる
    ret1, frame1 = cap1.read()

    # retがTrueじゃなければ、break
    if not ret1:
        break
    else:
        # X軸、Y軸、または両方の軸を中心に反転
        # 0:X軸を中心に反転(上下反転)
        # 1:Y軸を中心に反転(左右反転)
        # -1:両軸を中心に反転(上下左右反転)
        frame1 = cv2.flip(frame1, 0)

        #フレームのサイズ変更
        frame1 = cv2.resize(frame1, dsize=(320, 240))

        # VideoWriterで設定した内容を元に反転したframe1を書き込む
        # 読み込んだ動画と、設定しているフレームサイズが違うと、保存できない.(できていても、再生できない)
        out.write(frame1)

        # フレームをcaputreという名前のWindowで表示
        # 逆さで表示される
        cv2.imshow('capture1', frame1)

        # escキーが押された場合、ブレークしてwhileを抜ける
        # 0にすると、キーを受け付けるまで、待機してしまうため、フレームが更新されない
        # そのため、適切な数値を振る必要がある
        # 今回の場合は、30msecに設定
        if cv2.waitKey(30) & 0xFF == 27:
            break

# ビデオファイルまたは、キャプチャデバイスを閉じる
cap1.release()
out.release()

# 表示している画面を破棄
cv2.destroyAllWindows()
