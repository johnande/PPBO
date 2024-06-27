from collections import namedtuple

# Membuat namedtuple Kecepatan
Kecepatan = namedtuple("Kecepatan", ["jarak", "waktu"])

# Fungsi untuk menghitung kecepatan
def hitung_kecepatan(kecepatan):
    return kecepatan.jarak / kecepatan.waktu

# Main program
jarak = float(input("Masukkan jarak (km): "))
waktu = float(input("Masukkan waktu tempuh (jam): "))

# Membuat objek namedtuple Kecepatan
kecepatan = Kecepatan(jarak, waktu)

# Menghitung kecepatan menggunakan fungsi hitung_kecepatan
hasil_kecepatan = hitung_kecepatan(kecepatan)

# Menampilkan output
print(f"\nKecepatan: {hasil_kecepatan} km/jam")
