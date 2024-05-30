from collections import namedtuple

# (a) Buatlah namedtuple dengan nama Koordinat yang memiliki dua elemen dengan nama field x dan y!
Koordinat = namedtuple('Koordinat', 'x y')

# (b) Selanjutnya, buatlah instance dari namedtuple Koordinat dengan nama titik1 dengan nilai x = 2 dan y = 4!
titik1 = Koordinat(x=2, y=4)

# (c) Panggil elemen namedtuple titik1 dengan 3 cara yaitu menggunakan indeks elemen, field name, dan getattr()!
print('Menggunakan indeks elemen:', titik1[0], titik1[1])  # Output: Menggunakan indeks elemen: 2 4
print('Menggunakan field name:', titik1.x, titik1.y)  # Output: Menggunakan field name: 2 4
print('Menggunakan getattr():', getattr(titik1, 'x'), getattr(titik1, 'y'))  # Output: Menggunakan getattr(): 2 4