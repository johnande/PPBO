from collections import namedtuple

# a. Buat namedtuple dengan nama Koordinat yang memiliki dua elemen dengan nama field x dan y
Koordinat = namedtuple('Koordinat', ['x', 'y'])

# b. Buat instance dari namedtuple Koordinat dengan nama titik1 dengan nilai x = 2 dan y = 4
titik1 = Koordinat(x=2, y=4)

# c. Panggil elemen namedtuple titik1 dengan 3 cara
#    1. Menggunakan indeks elemen
print("Menggunakan indeks elemen:")
print("Nilai x:", titik1[0])

#    2. Menggunakan field name
print("\nMenggunakan field name:")
print("Nilai y:", titik1.y)

#    3. Menggunakan getattr()
print("\nMenggunakan getattr():")
print("Nilai x:", getattr(titik1, 'x'))
