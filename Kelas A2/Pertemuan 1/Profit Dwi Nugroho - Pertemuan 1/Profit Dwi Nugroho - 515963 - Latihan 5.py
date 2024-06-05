import math

# Input jari-jari dari pengguna
jari_jari_input = float(input("Masukkan panjang jari-jari lingkaran: "))

# Menghitung luas dan keliling lingkaran
def hitung_luas_lingkaran(jari_jari):
  luas = math.pi * jari_jari ** 2
  return luas

def hitung_keliling_lingkaran(jari_jari):
  keliling = 2 * math.pi * jari_jari
  return keliling

# Menampilkan hasil
luas = hitung_luas_lingkaran(jari_jari_input)
keliling = hitung_keliling_lingkaran(jari_jari_input)

print(f"Luas lingkaran dengan jari-jari {jari_jari_input} adalah: {luas:.2f}")
print(f"Keliling lingkaran dengan jari-jari {jari_jari_input} adalah: {keliling:.2f}")