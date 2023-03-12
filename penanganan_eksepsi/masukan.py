while True:
    try:
        masukan = input('Masukkan Bilangan : ')
        bilangan = int(masukan)
        break
    except ValueError:
        print('Salah dalam Memasukkan Bilangan')

print('bilangan = ', bilangan)