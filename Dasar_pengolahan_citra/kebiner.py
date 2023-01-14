# Konversi ke citra biner

import cv2

citra = cv2.imread('', cv2.IMREAD_GRAYSCALE)
ambang, binerA = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY_INV)
ambang, binerB = cv2.threshold(citra, 128, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Asli', citra)
cv2.imshow('THESH_BINERY', binerA)
cv2.imshow("THRESH_BINERY_INV", binerB)

cv2.waitKey(0)