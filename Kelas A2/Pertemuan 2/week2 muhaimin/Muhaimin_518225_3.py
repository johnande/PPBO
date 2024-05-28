class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        luas = self.sisi ** 2
        return luas

    def hitung_keliling(self):
        keliling = 4 * self.sisi
        return keliling

# Input sisi dari pengguna
sisi_persegi = float(input("Masukkan panjang sisi persegi: "))

# Membuat objek Persegi
persegi1 = Persegi(sisi_persegi)

# Menghitung luas dan keliling
luas_persegi = persegi1.hitung_luas()
keliling_persegi = persegi1.hitung_keliling()

# Menampilkan hasil
print(f"Luas persegi dengan sisi {sisi_persegi} adalah: {luas_persegi}")
print(f"Keliling persegi dengan sisi {sisi_persegi} adalah: {keliling_persegi}")
