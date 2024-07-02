from collections import namedtuple
Koordinat = namedtuple('titik1', ['x', 'y'])

Koordinat1 = Koordinat(x = '1', y = '4')

#akses elemen menggunakan indeks
print("Koordinat :", Koordinat1[0:2])
#akses elemen menggunakan nama atribut
print("x :", Koordinat1.x)
#akses elemen menggunakan getattr
print("y :", getattr(Koordinat1, "y"))