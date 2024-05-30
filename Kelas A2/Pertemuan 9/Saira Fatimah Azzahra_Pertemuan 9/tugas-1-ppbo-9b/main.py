from collections import namedtuple

#Membuat namedtuple koordinat
Koordinat = namedtuple('Koordinat', ['x', 'y'])

#Membuat instance titik1
titik1 = Koordinat(2,4)

#Memanggil elemen namedtuple dengan indeks elemen
print("Pemanggilan elemen dengan indeks elemen")
print("Nilai x:", titik1[0])
print("Nilai y:", titik1[1])

#Memanggil elemen namedtuple dengan field name
print("Pemanggilan elemen dengan field name")
print("Nilai x:", titik1.x)
print("Nilai y:", titik1.y)

#Memanggil elemen namedtuple dengan getattr()
print("Pemanggilan elemen dengan getattr():")
print("Nilai x:", getattr(titik1, 'x'))
print("Nilai y:", getattr(titik1, 'y'))


