# pengunaan pass pada except

infoMobil = ["Avanza", 2018, "Biru",1300,5]
jumblah = 0

for nilai in infoMobil:
    try:
        bilangan = int(nilai)
        jumblah = jumblah+1
    except ValueError:
        pass
print('jumbla elemen berupa bilangan : ', jumblah)