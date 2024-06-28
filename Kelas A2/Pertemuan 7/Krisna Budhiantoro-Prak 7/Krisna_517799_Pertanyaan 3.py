from collections import namedtuple

# a. Membuat namedtuple dengan nama Koordinat yang memiliki dua elemen x dan y
Koordinat = namedtuple('Koordinat', ['x', 'y'])

# b. Membuat instance dari namedtuple Koordinat dengan nilai x = 2 dan y = 4
titik1 = Koordinat(x=2, y=4)

# c. Memanggil elemen namedtuple titik1 dengan 3 cara: menggunakan indeks elemen, field name, dan getattr()
# Menggunakan indeks elemen
print("Menggunakan indeks elemen:")
print("Nilai x:", titik1[0])
print("Nilai y:", titik1[1])

# Menggunakan field name
print("\nMenggunakan field name:")
print("Nilai x:", titik1.x)
print("Nilai y:", titik1.y)

# Menggunakan getattr()
print("\nMenggunakan getattr():")
print("Nilai x:", getattr(titik1, 'x'))
print("Nilai y:", getattr(titik1, 'y'))
