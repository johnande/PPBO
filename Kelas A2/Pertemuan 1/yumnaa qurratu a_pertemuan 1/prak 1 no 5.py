import math

def hitung_luas_lingkaran(jari_jari):
    luas = math.pi * jari_jari**2
    return luas

def hitung_keliling_lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari
    return keliling

def main():
    # Input jari-jari dari pengguna
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))

    # Hitung luas dan keliling lingkaran
    luas = hitung_luas_lingkaran(jari_jari)
    keliling = hitung_keliling_lingkaran(jari_jari)

    # Tampilkan hasil
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}")
    print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling:.2f}")

if __name__ == "__main__":
    main()
