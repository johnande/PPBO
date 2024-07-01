from collections import namedtuple

Buah = namedtuple('Buah', ['nama', 'warna', 'harga'])

apel = Buah(nama='Apel', warna='Merah', harga=5000)
jeruk = Buah(nama='Jeruk', warna='Oranye', harga=7000)
mangga = Buah(nama='Mangga', warna='Hijau', harga=10000)

print("Informasi Buah:")
print("Nama:", apel.nama, "- Warna:", apel.warna, "- Harga:", apel.harga)
print("Nama:", jeruk.nama, "- Warna:", jeruk.warna, "- Harga:", jeruk.harga)
print("Nama:", mangga.nama, "- Warna:", mangga.warna, "- Harga:", mangga.harga)
