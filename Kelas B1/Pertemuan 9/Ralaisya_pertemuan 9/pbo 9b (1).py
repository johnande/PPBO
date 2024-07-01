from collections import namedtuple

# a. Membuat namedtuple Koordinat dengan field x dan y
Koordinat = namedtuple('Koordinat', ['x', 'y'])

# b. Membuat instance namedtuple Koordinat dengan nama titik1
titik1 = Koordinat(x=2, y=4)

# c. Mengakses elemen namedtuple titik1 dengan 3 cara
# Menggunakan indeks elemen
print("Menggunakan indeks elemen:")
print("Nilai x:", titik1[0])  # Output: 2
print("Nilai y:", titik1[1])  # Output: 4

# Menggunakan field name
print("\nMenggunakan field name:")
print("Nilai x:", titik1.x)  # Output: 2
print("Nilai y:", titik1.y)  # Output: 4

# Menggunakan getattr()
print("\nMenggunakan getattr():")
print("Nilai x:", getattr(titik1, 'x'))  # Output: 2
print("Nilai y:", getattr(titik1, 'y'))  # Output: 4
