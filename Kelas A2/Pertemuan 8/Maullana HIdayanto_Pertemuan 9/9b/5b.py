from collections import namedtuple

Buku = namedtuple('Buku', ['Judul', 'Penulis'])

buku1 = Buku(Judul='Harry Potter', Penulis='JK Rowling')

print(buku1.Judul)  
print(buku1.Penulis)  
