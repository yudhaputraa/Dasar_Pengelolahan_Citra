# Contoh Translasi Citra

import cv2
import numpy as np

citra = cv2.imread('../taipei101.png')
JumBaris, JumKolom = citra.shape[:2]

matriks = np.float32([[1,0,50], [0,1,100]])
hasil = cv2.warpAffine(citra, matriks, (JumKolom, JumBaris))

cv2.imshow('Hasil translasi', hasil)
cv2.waitKey()