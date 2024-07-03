from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

titik1 = Koordinat('2', '4')
#akses elemen menggunakan indeks
print("Nilai x :", titik1[0])
#akses elemen menggunakan nama atribut
print("Nilai x :", titik1.x)
#akses elemen menggunakan getattr
print("Nilai y :", getattr(titik1, "y"))
