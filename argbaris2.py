# Contoh pembacaan argumen baris perintah
#  versi 2

import sys

if len(sys.argv) == 1 :
    print('Tidak ada argumen baris printa')
else:
    jumArgumen = len(sys.argv)
    print('Argumen:')
    for indeks in range(1, jumArgumen):
        print(indeks, '.', sys.argv[indeks], sep='')