# Pembacaan baboon.png dalam bentuk skala keabu-abuan.

import cv2

# IMREAD_GRAYSCALE() membuat gambar menjadi abu-abu.
citra = cv2.imread('Baboon.png', cv2.IMREAD_GRAYSCALE)
if not citra is None:
    cv2.imshow('Gambar Baboon.png', citra)
    cv2.waitKey(0)
    