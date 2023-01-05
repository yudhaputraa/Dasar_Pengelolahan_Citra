# contoh pengunnaan irisan utk memperoleh suatu bagian pd citra

import cv2

citra = cv2.imread('peppers.png')
# 30:240 = adalah baris
# 210:388 = adalah kolom
citra[30:240, 210:388] = [255,0,0]
cv2.imshow('Irisan', citra)
cv2.waitKey(0)