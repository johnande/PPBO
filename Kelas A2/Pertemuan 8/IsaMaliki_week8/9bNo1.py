from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

titik1 = Koordinat(2, 4)

# pemanggilan elemen menggunakan indeks elemen
print(f"x = {titik1[0]}, y = {titik1[1]}")

# pemanggilan elemen menggunakan field name
print(f"x = {titik1.x}, y = {titik1.y}")

# pemanggilan elemen menggunakan getattr
print(f"x = {getattr(titik1, 'x')}, y = {getattr(titik1, 'y')}")