class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas_persegi(self):
        return self.sisi * self.sisi

    def hitung_keliling_persegi(self):
        return 4 * self.sisi


sisi_persegi = float(input("Masukkan panjang sisi persegi: "))
persegi = Persegi(sisi_persegi)
print("Luas perseginya adalah", persegi.hitung_luas_persegi())
print("Keliling perseginya adalah:", persegi.hitung_keliling_persegi())
