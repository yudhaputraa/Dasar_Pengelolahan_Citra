# penggabungan citra goldhill dan baboon

import cv2

goldhill = cv2.imread('goldhill2.jpg')
goldhill =  cv2.resize(goldhill, (512, 512))
baboon = cv2.imread('Baboon.png')
baboon =  cv2.resize(baboon, (512, 512))
hasil = cv2.add(baboon, goldhill)

hasilA = cv2.addWeighted(baboon, 0.5, goldhill, 0.5, 0)
cv2.imshow('alfa: 0.5, beta: 0.5, gamma: 0', hasilA)

hasilB = cv2.addWeighted(baboon, 0.7, goldhill, 0.3, 0)
cv2.imshow('alfa: 0.7, beta: 0.3, gamma: 0', hasilB)

hasilC = cv2.addWeighted(baboon, 0.3, goldhill, 0.7, 0)
cv2.imshow('alfa: 0.3, beta: 0.7, gamma: 0', hasilC)

cv2.waitKey(0)