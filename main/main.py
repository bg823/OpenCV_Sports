import cv2
# ヒストグラム表示に使う
from matplotlib import pyplot as plt

# 今回はcandyの画像をカラーで読みこむ
# 画像が作業ディレクトリにある場合は、そのパスを、他のディレクトリにある場合は、フルパスをい入れる必要があります
# 1でカラー, 0でグレー, -1でアルファチャネルを含む画像を読み込みます
img = cv2.imread('/Users/h-nagaoka/Dev/OpenCV_Sports/images/candy.jpg', 1)

# 塗り潰しで表示
plt.hist(img.ravel(), 256, [0, 256])
#
plt.figure()


# colorのタプル
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    # colorのインデックスとbgrを格納
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    # ヒストグラムをプロット
    plt.plot(histr, color=col)
    # X軸を0-256の間でヒストグラム表を作る
    plt.xlim([0, 256])

# プロットの表示
plt.show()
