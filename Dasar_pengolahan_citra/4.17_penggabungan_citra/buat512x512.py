# Pembuatan citra berukuran 512 X 512 yg mengadung citra spaceman-color
import cv2
import numpy as np

# Buat citra berwarna hitam
citra = np.zeros((512, 512, 3), np.uint8)

spaceman = cv2.imread('spaceman.png', -1)
spaceman_resized = cv2.resize(spaceman, (512, 512))
# v2.resize utk mengubah ukuran gambar

jumBaris = spaceman_resized.shape[0]
jumKolom = spaceman_resized.shape[1]

citra[0:jumBaris, 0:jumKolom, :] = spaceman_resized[:, :, 0:3]
cv2.imshow('Hasil', citra)

cv2.waitKey(0)
