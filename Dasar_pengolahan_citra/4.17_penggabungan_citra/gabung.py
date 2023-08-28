# Penggabungan citra spaceman dgn goldhil

import cv2
import numpy as np

# buat citra berwarna hitam
citra = np.zeros((512,512,3), np.uint8)

spaceman = cv2.imread('spaceman.png', -1)
spaceman_resized = cv2.resize(spaceman, (512, 512))
# v2.resize utk mengubah ukuran gambar

jumBaris = spaceman_resized.shape[0]
jumKolom = spaceman_resized.shape[1]

citra[0:jumBaris, 0:jumKolom, :] = spaceman_resized[:, :, 0:3]

goldhill = cv2.imread('goldhill2.jpg')
goldhill_resized = cv2.resize(goldhill, (512, 512))  # ubah ukuran citra goldhill

hasil = cv2.add(goldhill_resized, citra)

cv2.imshow('Hasil',hasil)

cv2.waitKey(0)