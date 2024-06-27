from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

titik1 = Koordinat('2', '4')

#akses elemen menggunakan indeks
print("X :", titik1[0])
#akses elemen menggunakan nama atribut
print("Y :", titik1.y)
#akses elemen menggunakan getattr
print("x :", getattr(titik1, "x"))