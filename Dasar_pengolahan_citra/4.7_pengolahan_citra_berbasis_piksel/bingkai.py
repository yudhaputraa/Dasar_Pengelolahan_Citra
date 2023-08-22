# Contoh pemberian bingkai pd citra berskala keabu-abuan

import cv2

citra = cv2.imread('Baboon.png')

if citra is not None:
    print("Gambar berhasil dibaca.")
else:
    print("Gambar tidak dapat dibaca.")

hasil = citra.copy() # salin isi citra

# pengolahan citra
TEBAL =20
HITAM = 0

jumBaris = hasil.shape[0] # digunakan utk memeroleh jumlah baris
jumKolom = hasil.shape[1] # digunakan utk memeroleh jumlah kolom

# -- Bingkai di atas
for baris in range(TEBAL):
    for kolom in range(jumKolom):
        hasil[baris,kolom] = HITAM
        
# -- bingkai di bawah
for baris in range(jumBaris - TEBAL - 1, jumBaris):
    for kolom in range(jumKolom):
        hasil[baris, kolom] = HITAM

# -- Bingkai kiri
for baris in range(TEBAL, jumBaris - TEBAL - 1):
    for kolom in range(TEBAL):
        hasil[baris, kolom] = HITAM

# -- Bingkai kanan
for baris in range(TEBAL, jumBaris - TEBAL - 1):
    for kolom in range(jumKolom - TEBAL - 1, jumKolom):
        hasil[baris, kolom] = HITAM

cv2.imshow('gambar asal', citra)
cv2.imshow('gambar hasil', hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()