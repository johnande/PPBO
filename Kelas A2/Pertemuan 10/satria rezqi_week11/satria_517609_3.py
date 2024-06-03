from collections import namedtuple

koordinat = namedtuple("koordinat", ['x', 'y'])

titik1 = koordinat(2, 4)

print(titik1.x)
print(getattr(titik1, 'y'))
print(titik1[0])