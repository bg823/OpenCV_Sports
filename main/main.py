import cv2

# 今回はcandyの画像をカラーで読みこむ
# 画像が作業ディレクトリにある場合は、そのパスを、他のディレクトリにある場合は、フルパスをい入れる必要があります
# 1でカラー, 0でグレー, -1でアルファチャネルを含む画像を読み込みます
img = cv2.imread('your file dir/candy.jpg', 1)

# candy_imgというWindow名で読み込んだ画像を表示
cv2.imshow('candy_img', img)

# 何かしらのキーボードのキーが押されるまで、Windowを表示し続ける
cv2.waitKey(0)

# キーが押されたら、Windowを破棄する
cv2.destroyAllWindows()
