from collections import namedtuple

# Membuat namedtuple Koordinat dengan dua elemen x dan y
Koordinat = namedtuple('Koordinat', ['x', 'y'])

# Membuat instance dari namedtuple Koordinat dengan nilai x = 2 dan y = 4
titik1 = Koordinat(x=2, y=4)

# Mengakses elemen namedtuple titik1 dengan indeks elemen
print("Menggunakan indeks elemen:")
print("Nilai x:", titik1[0])
print("Nilai y:", titik1[1])

# Mengakses elemen namedtuple titik1 dengan field name
print("\nMenggunakan field name:")
print("Nilai x:", titik1.x)
print("Nilai y:", titik1.y)

# Mengakses elemen namedtuple titik1 dengan getattr()
print("\nMenggunakan getattr():")
print("Nilai x:", getattr(titik1, 'x'))
print("Nilai y:", getattr(titik1, 'y'))
