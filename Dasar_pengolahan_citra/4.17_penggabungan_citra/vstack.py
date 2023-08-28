# penggabungan dua gambar secara bertumpukan

import cv2
import numpy as np

goldhill = cv2.imread('goldhill2.jpg')
citraA =  cv2.resize(goldhill, (512, 512))
baboon = cv2.imread('Baboon.png')
citraB =  cv2.resize(baboon, (512, 512))

hasil = np.vstack((citraA,citraB))

# Tampilkan hasilnya
cv2.imshow('hasil', hasil)

cv2.waitKey(0)