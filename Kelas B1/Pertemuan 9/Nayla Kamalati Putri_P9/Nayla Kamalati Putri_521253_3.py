#No3

from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

def akses_titik(titik):
  print("Menggunakan indeks elemen:")
  print(f"Nilai x: {titik[0]}")
  print(f"Nilai y: {titik[1]}")

  print("\nMenggunakan field name:")
  print(f"Nilai x: {titik.x}")
  print(f"Nilai y: {titik.y}")

  print("\nMenggunakan getattr():")
  print(f"Nilai x: {getattr(titik, 'x')}")
  print(f"Nilai y: {getattr(titik, 'y')}")

titik1 = Koordinat(2, 4)

akses_titik(titik1)
