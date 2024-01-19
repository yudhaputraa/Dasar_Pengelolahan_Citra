"""
Pembengkokan citra adalah suatu transformasi yang 
melakukan penggeserkan piksel ke kiri, ke kanan, 
ke atas, atau ke bawah secara bertahap mengikuti posisi x dan y.
"""

# Contoh Pembengkokan Citra
#   Secara Horizontal

import cv2
import numpy as np
import math
citra = cv2.imread('../taipei101.png')
JumBaris, JumKolom = citra.shape[:2]

matriks = np.float32([[1,0.25,0],[0,1,0]])
""" 
Agar bagian kiri terpotong, translasi pd arah 
mendaftar perlu diatur, misalnya 180 seperti berikut:
"""
# matriks = np.float32([[1,-0.25,180],[0,1,0]])
hasil = cv2.warpAffine(citra, matriks, (int(1.4*JumKolom), JumBaris))

gab = np.hstack((citra,hasil))
cv2.imshow('Hasil Pembengkokan', gab)
cv2.waitKey()