# Contoh putText()

import cv2

citra = cv2.imread('Baboon.png')

# buat tulisan 
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX + cv2.FONT_ITALIC
"""
Jenis font digunakan dpt berupa salah satu dari berikut:
- FONT_HERSHEY_COMPLEX
- FONT_HERSHEY_COMPLEX_SMALL
- FONT_HERSHEY_DUPLEX
- FONT_HERSHEY_PLAIN
- FONT_HERSHEY_SCRIPT_COMPLEX
- FONT_HERSHEY_SCRIPT_SIMPLEX
- FONT_HERSHEY_SIMPLEX
- FONT_HERSHEY_TRIPLEX

"""
cv2.putText(citra, 'Baboon', (10,500), font,4,(0,0,0),10)

# Tampilkan citra
cv2.imshow('Hasil',citra)

cv2.waitKey(0)