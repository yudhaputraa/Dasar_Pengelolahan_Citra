"""
 Contoh berikut menunjukkan cara membengkokkan citra secara vertikal:
"""

# Contoh Pembengkokan Citra
#   Secara Vertikal

import cv2
import numpy as np
import math
citra = cv2.imread('../taipei101.png')
JumBaris, JumKolom = citra.shape[:2]

matriks = np.float32([[1,0,0],[0.25,1,0]])
""" 
Apabila matriks di ubah dgn nilai pembengkokan horizontal
menjadi negatif seperti berikut, pembangkokan yang terjadi 
berlawanan dgn contoh sebelum ini :

# matriks = np.float32([[1,0,0],[-0.25,1,0]])

Apabila matriks di ubah dgn nilai pembengkokan horizontal
menjadi negatif seperti berikut, pembangkokan yang terjadi 
berlawanan dgn contoh sebelum ini :

# matriks = np.float32([[1,0.1,0],[0.25,1,0]])
"""
hasil = cv2.warpAffine(citra, matriks, (int(1.4*JumKolom), JumBaris))

gab = np.hstack((citra,hasil))
cv2.imshow('Hasil Pembengkokan', gab)
cv2.waitKey()