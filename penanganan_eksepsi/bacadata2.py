# pembacaan data berkas teks mengunakan pernyataan try..finally

import sys

if len(sys.argv) == 1:
    print('masukkan nama berkas yang ingin dibaca')
else:
    berkas = sys.argv[1]

    try:
        pegangan = open(berkas, 'r')
        konten = pegangan.read()
        print('isi berkas:')
        print(konten)
    except:
        pass
    finally:
        print('Operasi pembacaan berkas telah berakhir')
    print('*****')