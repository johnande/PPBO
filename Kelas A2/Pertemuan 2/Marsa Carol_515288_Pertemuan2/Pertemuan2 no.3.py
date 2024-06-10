class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi

def main():
    # Input panjang sisi dari pengguna
    panjang_sisi = float(input("Masukkan panjang sisi persegi: "))

    # Buat objek dari kelas 'Persegi'
    persegi1 = Persegi(panjang_sisi)

    # Hitung luas dan keliling persegi
    luas_persegi = persegi1.hitung_luas()
    keliling_persegi = persegi1.hitung_keliling()

    # Tampilkan hasil
    print(f"Luas persegi: {luas_persegi}")
    print(f"Keliling persegi: {keliling_persegi}")

if __name__ == "__main__":
    main()

