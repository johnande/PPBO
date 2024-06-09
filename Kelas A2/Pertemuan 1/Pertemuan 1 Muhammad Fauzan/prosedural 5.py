import math

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas_lingkaran = hitung_luas_lingkaran(jari_jari)
keliling_lingkaran = hitung_keliling_lingkaran(jari_jari)

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas_lingkaran:.2f}")
print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling_lingkaran:.2f}")
