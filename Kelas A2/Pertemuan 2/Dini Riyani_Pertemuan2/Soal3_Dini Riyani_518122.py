class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi

    def tampilkan_data(self):
      luas_persegi = self.hitung_luas()
      keliling_persegi = self.hitung_keliling()
      print(f"Luas persegi: {luas_persegi}")
      print(f"Keliling persegi: {keliling_persegi}")

panjang_sisi = float(input("Masukkan panjang sisi persegi: "))
persegi1 = Persegi(panjang_sisi)
persegi1.tampilkan_data()