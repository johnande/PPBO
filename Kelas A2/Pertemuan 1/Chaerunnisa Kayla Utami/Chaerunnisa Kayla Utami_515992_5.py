import math

def hitung_luas(jari_jari):
    return math.pi * jari_jari ** 2

def hitung_keliling(jari_jari):
    return 2 * math.pi * jari_jari

# Membaca input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Menghitung luas lingkaran
luas = hitung_luas(jari_jari)
print("Luas lingkaran:", luas)

# Menghitung keliling lingkaran
keliling = hitung_keliling(jari_jari)
print("Keliling lingkaran:", keliling)
