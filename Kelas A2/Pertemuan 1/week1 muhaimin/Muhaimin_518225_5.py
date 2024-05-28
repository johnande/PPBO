import math

# Minta input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Hitung keliling lingkaran
keliling = 2 * math.pi * jari_jari

# Hitung luas lingkaran
luas = math.pi * (jari_jari ** 2)

# Tampilkan hasil
print(f"Keliling lingkaran: {keliling:.2f}")
print(f"Luas lingkaran: {luas:.2f}")
