# pengaturan kecerahan

import cv2

citra = cv2.imread('goldhill.jpg', 0)
cv2.imshow('gambar asli', citra)

hasil = 255 - citra
cv2.imshow('Citra Hasil', hasil)
cv2.waitKey(0)