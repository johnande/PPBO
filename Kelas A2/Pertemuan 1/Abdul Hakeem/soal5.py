import math

r = float(input("Masukkan jari-jari lingkaran: "))
luas = math.pi * r ** 2
keliling = 2 * math.pi * r

print("Luas lingkaran:", math.trunc(luas), "\nKeliling lingkaran:", math.trunc(keliling))