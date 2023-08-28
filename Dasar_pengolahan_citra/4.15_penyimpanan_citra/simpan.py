# Penyimpanan citra ke berkas hasil.png

import cv2
import sys

citra = cv2.imread('Baboon.png', 0)

hasil = 255 - citra
cv2.imwrite('Hasil.png', hasil)

print('citra telah disimpan di hasil,png')