import math

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

try:
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
    if jari_jari < 0:
        print("Jari-jari tidak boleh negatif.")
    else:
        luas = hitung_luas_lingkaran(jari_jari)
        keliling = hitung_keliling_lingkaran(jari_jari)
        print("Luas lingkaran:", luas)
        print("Keliling lingkaran:", keliling)
except ValueError:
    print("Input yang dimasukkan bukan angka.")

