# Penggabungan citra spaceman dgn goldhill menggunakan komponen alfa

import cv2
import numpy as np

# Buat citra berwarna hitam
citra = np.zeros((512, 512, 3), np.uint8)
alfa = np.zeros((512, 512), np.uint8)

spaceman = cv2.imread('spaceman.png', -1)
spaceman_resized = cv2.resize(spaceman, (512, 512))

jumBaris = spaceman_resized.shape[0]
jumKolom = spaceman_resized.shape[1]

citra[0:jumBaris, 0:jumKolom, :] = spaceman_resized[:, :, 0:3]
alfa[0:jumBaris, 0:jumKolom] = spaceman_resized[:, :, 3]
cadar = cv2.merge((alfa, alfa, alfa))
kebalikan = cv2.bitwise_not(cadar)

goldhill = cv2.imread('goldhill2.jpg')
goldhill_resized = cv2.resize(goldhill, (512, 512))  # ubah ukuran citra goldhill

hasil_and = cv2.bitwise_and(goldhill_resized, kebalikan)  # gunakan citra goldhill yang sudah diubah ukuran
cv2.imshow('Hasil and', hasil_and)

hasil_add = cv2.add(hasil_and, citra)
cv2.imshow('Hasil add', hasil_add)

cv2.waitKey(0)

