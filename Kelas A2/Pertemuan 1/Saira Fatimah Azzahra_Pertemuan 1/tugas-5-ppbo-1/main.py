import math

def hitung_luas(r):
    return math.pi * r**2

def hitung_keliling(r):
    return 2 * math.pi * r

r = float(input("Masukkan jari-jari lingkaran: "))

luas = hitung_luas(r)
keliling = hitung_keliling(r)

print("Luas lingkaran: ", luas)
print("Keliling lingkaran: ", keliling)