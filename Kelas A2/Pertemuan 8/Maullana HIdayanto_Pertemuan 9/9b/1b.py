from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

titik1 = Koordinat(6, 9)

# indeks elemen
print(titik1[0], titik1[1])

# field name
print(titik1.x, titik1.y)

# getattr()
print(getattr(titik1, 'x'), getattr(titik1, 'y'))
