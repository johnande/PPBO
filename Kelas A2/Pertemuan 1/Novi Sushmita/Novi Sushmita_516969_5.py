import math

print("Program Menghitung Keliling dan Luas Lingkaran")

jari_jari= int(input("Masukkan jari-jari lingkaran: "))

keliling = 2 * math.pi * jari_jari
print("Keliling lingkaran: ", keliling)

luas = math.pi * jari_jari * jari_jari
print("Luas lingkaran : ", luas)