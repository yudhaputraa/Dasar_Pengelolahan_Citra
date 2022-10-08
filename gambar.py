# Contoh menambilkan gambar dgn cv2 dan pengambilan dgn sys
import cv2
import sys

if len(sys.argv) == 1:
    print('Masukan nama Berkas gambar')
else:
    berkas = sys.argv[1]
    citra = cv2.imread(berkas)
    if citra is None:
        print("Tidak dapat membaca berkas", berkas)
    else:
        cv2.imshow('Gambar', citra)
        cv2.waitKey(0)