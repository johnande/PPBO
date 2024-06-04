from collections import namedtuple

Koordinat = namedtuple( 'Koordinat', ['x', 'y'])

titik1 = Koordinat(x=2, y=4)

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