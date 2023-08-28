# Penulisan teks di tengah citra

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

        FONT = cv2.FONT_HERSHEY_DUPLEX
        UKURAN = 2
        KETEBALAN = 1

        info1, info2 = cv2.getTextSize(berkas, FONT, UKURAN, KETEBALAN)

        posisix = (jumBaris - info1[0]) // 2
        posisiy = (jumBaris - info1[1]) // 2 + info1[1]

        print(jumBaris, jumKolom, posisix, posisiy)
        print(info1, info2)

        cv2.putText(citra, berkas, (posisix, posisiy), FONT, UKURAN, (255,255,255), KETEBALAN)

        # Tampilkan citra
        cv2.imshow('Hasil', citra)

        cv2.waitKey(0)
