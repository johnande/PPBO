from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

titik1 = Koordinat(x=2, y=4)

print("Menggunakan indeks elemen:", titik1[0], titik1[1])
print("Menggunakan field name:", titik1.x, titik1.y)
print("Menggunakan getattr():", getattr(titik1, 'x'), getattr(titik1, 'y'))