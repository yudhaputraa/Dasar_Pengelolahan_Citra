# contoh penggunaan irisan utk memproleh suatu bagian pd citra

import cv2

citra = cv2.imread('peppers.png')
bagianA = citra[0:100, ...]
# jika mengunakan ... utk kolom tidak bisa utk mengatasinya mengunakan :
bagianB = citra[: , 250:] 

cv2.imshow('Bagian A', bagianA)
cv2.imshow('Bagian B', bagianB)
cv2.waitKey(0)