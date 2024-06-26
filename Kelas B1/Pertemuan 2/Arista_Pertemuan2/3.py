class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi ** 2
    
    def hitung_keliling(self):
        return 4 * self.sisi

# Input panjang sisi persegi
sisi_persegi = float(input("Masukkan panjang sisi persegi: "))

# Membuat objek Persegi
persegi_saya = Persegi(sisi_persegi)

# Menghitung luas dan keliling persegi
luas = persegi_saya.hitung_luas()
keliling = persegi_saya.hitung_keliling()

# Menampilkan hasil perhitungan
print(f"Luas persegi: {luas}")
print(f"Keliling persegi: {keliling}")
