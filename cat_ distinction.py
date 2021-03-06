import cv2
import numpy as np
import math 
import matplotlib.pyplot as plt


from google.colab import files
uploaded_file = files.upload()

# 入力画像を読み込み
img = cv2.imread("読み込んだ画像の名前")

# カスケード型識別器の読み込み
cat_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")

# 画像をグレーに変換
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 猫の顔領域の探索
cat_list = cat_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

# 猫の顔領域を赤色の矩形で囲む
for (x, y, w, h) in cat_list:
    color = (0, 0, 225) #BGR
    pen_w = 2
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)

    #猫の領域を取り出しリストへ
    cat = cat_list[0]

    boxFromX = cat[0]
    boxFromY = cat[1]
    boxToX = int(cat[0]) + int(cat[2])
    boxToY = int(cat[1]) + int(cat[3])

    imgBox = img[boxFromY: boxToY, boxFromX: boxToX]

    #領域内のRGBの平均値を代入
    b = imgBox.T[0].flatten().mean()
    g = imgBox.T[1].flatten().mean()
    r = imgBox.T[2].flatten().mean()

    #小数点切り捨て
    b = math.floor(b)  
    g = math.floor(g)  
    r = math.floor(r)

    #黒猫か否か判断
    if b < 60 and g < 60 and r < 60:
      print("黒猫です")
    else:
      print("黒猫ではありません") 

# 結果の出力
cv2.imwrite("cat_out.jpg", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show("cat_out.jpg")
