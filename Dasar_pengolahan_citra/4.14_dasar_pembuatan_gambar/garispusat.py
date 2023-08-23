# pembuatan garis tegak dan mendaftar memalui titik tengah citra.

import cv2
import sys

if len(sys.argv) == 1:
    print('Masukan nama berkas gambar')
else:
    berkas = sys.argv[1]
    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
    if citra is None:
        print('Tidak dpt membaca berkas', berkas)
    else:
        jumBaris = citra.shape[0]
        jumKolom = citra.shape[1]
        xTengah = jumKolom // 2
        yTengah = jumBaris // 2
        
        # Buat garis tegak.
        cv2.line(citra, (xTengah, 0), (yTengah, jumBaris - 1), [128,128,128], 5)
        #cv2.arrowedLine(citra, (xTengah, 0), (yTengah, jumBaris - 1), [128,128,128], 5)

        # Buat garis mendatar.
        cv2.line(citra, (0, yTengah), (jumKolom - 1, yTengah), [128,128,128], 5)
        #cv2.arrowedLine(citra, (0, yTengah), (jumKolom - 1, yTengah), [128,128,128], 5)

        # Tampilkan citra.
        cv2.imshow('hasil', citra)

        cv2.waitKey(0)

        # arrowedLine() fungsi ini digunakan utk membuat garis dgn ujung akhir dilengkapi mata anak panah.