# Konversi ke citra biner menggunakan metode otsu

import cv2

citra = cv2.imread('airlane.png', cv2.IMREAD_GRAYSCALE)
ambang, biner =  cv2.threshold(citra, 128, 255, cv2.THRESH_BINER + cv2.THRESH_OTSU)

cv2.imshow('Asli', citra)
cv2.imshow('Otsu - nilai ambang = ' + str(int(ambang)),biner)

cv2.waitKey(0)