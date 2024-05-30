from collections import namedtuple

koordinat = namedtuple('koordinat', ['x', 'y'])

titik_satu = koordinat(2,4)


print(titik_satu[0], titik_satu[1])

print(titik_satu.x, titik_satu.y)
 
print(getattr(titik_satu, 'x'), getattr(titik_satu, 'y'))


