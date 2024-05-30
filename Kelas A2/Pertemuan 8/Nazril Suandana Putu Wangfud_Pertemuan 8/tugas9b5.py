from collections import namedtuple

# Membuat namedtuple dengan nama 'Planet' yang memiliki dua ciri": 'nama' dan 'warna'
Planet = namedtuple('Planet', ['nama', 'warna'])

# Membuat objek Planet
Planet1 = Planet('Bumi', 'Biru')
Planet2 = Planet('Mars', 'Merah')

# Mengakses nilai-nilai dalam namedtuple
print("Planet 1 - Nama planet:", Planet1.nama)
print("Planet 1 - warna planet:", Planet1.warna)
print("Planet 2 - Nama planet:", Planet2.nama)
print("Planet 2 - warna planet:", Planet2.warna)

# Menggunakan metode _asdict() untuk mengonversi namedtuple ke dalam kamus
print("Planet 1:", Planet1._asdict())
print("Planet 2:", Planet2._asdict())