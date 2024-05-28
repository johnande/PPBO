from collections import namedtuple

# a. Buat namedtuple Koordinat dengan field x dan y
Koordinat = namedtuple('Koordinat', ['x', 'y'])

# b. Buat instance namedtuple titik1 dengan nilai x = 2 dan y = 4
titik1 = Koordinat(x=2, y=4)

# c. Panggil elemen namedtuple titik1 dengan 3 cara
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
