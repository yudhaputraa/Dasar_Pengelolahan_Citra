# Pemisahan kanal citra berwarna

import cv2
import numpy as np

citra = cv2.imread('peppers.png')

# Buat citra berwarna hitam
jumBaris = citra.shape[0]
jumKolom = citra.shape[1]

# Matriks berisi nol
nol = np.zeros((jumBaris, jumKolom), np.uint8)

biru, hijau, merah = cv2.split(citra)
citraB = cv2.merge((biru, nol, nol))
citraG = cv2.merge((nol, hijau, nol))
citraR = cv2.merge((nol, nol, merah))

cv2.imshow('Kanal biru',citraB)
cv2.imshow('Kanal hijau', citraG)
cv2.imshow('Kanal Merah', citraR)

cv2.waitKey(0)