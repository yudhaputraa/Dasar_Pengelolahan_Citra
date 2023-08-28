# penggabungan citra goldhill dan baboon

import cv2

goldhill = cv2.imread('goldhill2.jpg')
goldhill =  cv2.resize(goldhill, (512, 512))
baboon = cv2.imread('Baboon.png')
baboon =  cv2.resize(baboon, (512, 512))
hasil = cv2.add(baboon, goldhill)

cv2.imshow('Hasil', hasil)

cv2.waitKey(0)