import math

def hitung_keliling_luas_lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari
    luas = math.pi * (jari_jari ** 2)
    return keliling, luas

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

keliling, luas = hitung_keliling_luas_lingkaran(jari_jari)

print(f"Keliling lingkaran: {keliling:.2f}")
print(f"Luas lingkaran: {luas:.2f}")
