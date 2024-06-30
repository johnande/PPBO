from collections import namedtuple

Koordinat = namedtuple('Koordinat', 'x y')
titik1 = Koordinat(2, 4)

print(f'Menggunakan indeks elemen:')
print(f'x = {titik1[0]}')
print(f'y = {titik1[1]}')

print(f'\nMenggunakan field name:')
print(f'x = {titik1.x}')
print(f'y = {titik1.y}')

print(f'\nMenggunakan getattr():')
print(f'x = {getattr(titik1, "x")}')
print(f'y = {getattr(titik1, "y")}')