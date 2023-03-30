# contoh pengunnaan irisan utk memperoleh suatu bagian pd citra

import cv2

citra = cv2.imread('peppers.png')
# 30:240 = adalah baris
# 210:388 = adalah kolom
bagian = citra[30:240, 210:388]
cv2.imshow('Irisan', bagian)
cv2.waitKey(0)