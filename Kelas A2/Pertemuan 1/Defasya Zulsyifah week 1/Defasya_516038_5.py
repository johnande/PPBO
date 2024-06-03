import math

def hitung_luas(jari_jari):
    return math.pi * jari_jari**2

def hitung_keliling(jari_jari):
    return 2 * math.pi * jari_jari

def main():
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))

    luas = hitung_luas(jari_jari)
    keliling = hitung_keliling(jari_jari)

    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)

if __name__ == "__main__":
    main()
