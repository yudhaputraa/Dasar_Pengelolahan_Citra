# mengatur kecerahan

import cv2

citra = cv2.imread('goldhill.jpg',0)
cv2.imshow('Gambar Asli', citra)

hasil = citra + 50
cv2.imshow('Citra hasil',hasil)
cv2.waitKey(0)