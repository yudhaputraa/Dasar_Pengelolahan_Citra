# Contoh rotasi citra

import cv2
import numpy as np

citra = cv2.imread('../taipei101.png')
JumBaris, JumKolom = citra.shape[:2]

matriks = cv2.getRotationMatrix2D((JumKolom // 2, JumBaris // 2), -15, 1)
hasil = cv2.warpAffine(citra, matriks, (JumKolom, JumBaris))

cv2.imshow('Hasil translasi', hasil)
cv2.waitKey()