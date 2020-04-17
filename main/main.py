import cv2
# ヒストグラム表示に使う
from matplotlib import pyplot as plt

# 今回はcandyの画像をカラーで読みこむ
# 画像が作業ディレクトリにある場合は、そのパスを、他のディレクトリにある場合は、フルパスをい入れる必要があります
# 1でカラー, 0でグレー, -1でアルファチャネルを含む画像を読み込みます
img = cv2.imread('/your file path/gray_candy.jpg', 0)

# 塗り潰しで表示
plt.hist(img.ravel(), 256, [0, 256])
# プロットの保存
plt.savefig('result/gray_img_1.png')

<<<<<<< HEAD
# gray画像をヒストグラム表示させるために、計算
# 実線で表示
gray_img_2 = cv2.calcHist([img], [0], None, [256], [0, 256])
# 新しく図を作成
plt.figure()
# プロット作成
plt.plot(gray_img_2)
# プロットの保存
plt.savefig('result/gray_img_2.png')
=======
# colorのタプル
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    # colorのインデックスとbgrを格納
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    # ヒストグラムをプロット
    plt.plot(histr, color=col)
    # X軸を0-256の間でヒストグラム表を作る
    plt.xlim([0, 256])
>>>>>>> 5a79a2156ac0bcc76ad3d930999be163969c05a0

# プロットの表示
plt.show()
