#No7

from collections import namedtuple

gaji = ("Bintang", 6000, 2018)
print("Tuple biasa:")
print(gaji)

GajiKaryawan = namedtuple('GajiKaryawan', ['nama', 'gaji_pokok', 'tahun_masuk'])

bintang = GajiKaryawan(nama='Bintang', gaji_pokok=5000, tahun_masuk=2018)

print("\nGaji Bintang:")
print("Nama         :", bintang.nama)
print("Gaji Pokok   :", bintang.gaji_pokok)
print("Tahun Masuk  :", bintang.tahun_masuk)

print("\nTipe data:")
print("Tipe data gaji   :", type(gaji).__name__)
print("Tipe data bintang:", type(bintang).__name__)

