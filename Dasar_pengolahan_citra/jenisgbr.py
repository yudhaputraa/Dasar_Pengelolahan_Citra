# penetuan gambar sebagai gambar berwarna atau berskala abu-abuan

import cv2
import sys

if len(sys.argv) == 1:
    print('Masukan nama berkas gambar')
else:
    berkas =sys.argv[1]
    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
    if citra is None:
        print('Tidak membaca berkas', berkas)
    else: 
        info = citra.shape
        if len(info) == 2:
            print('citra berskala keabu-abuan : ', info)
        else:
            print('Citra berwarna : ', info)