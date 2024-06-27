import math

def hitung_luas_lingkaran(jari_jari):
    luas = math.pi * jari_jari**2
    return luas

def hitung_keliling_lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari
    return keliling

jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
    
if jari_jari < 0:
    print("Jari-jari tidak boleh negatif.")
else:
    luas = hitung_luas_lingkaran(jari_jari)
    keliling = hitung_keliling_lingkaran(jari_jari)

    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)
