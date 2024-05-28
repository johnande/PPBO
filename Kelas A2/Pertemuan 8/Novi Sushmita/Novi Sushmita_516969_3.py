from collections import namedtuple

Koordinat = namedtuple("Koordinat", ["x", "y"])

titik1 = Koordinat(x = 2, y = 4)

print("== Menggunakan indeks elemen ==")
print("Nilai x:", titik1[0])
print("Nilai y:", titik1[1])

print("== Menggunakan field name ==")
print("Nilai x:", titik1.x)
print("Nilai y:", titik1.y)

print("== Menggunakan getattr() ==")
print("Nilai x:", getattr(titik1, "x"))
print("Nilai y:", getattr(titik1, "y"))