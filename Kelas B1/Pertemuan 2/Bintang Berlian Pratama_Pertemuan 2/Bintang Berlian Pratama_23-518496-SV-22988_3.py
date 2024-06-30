class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.luas = sisi**2
        self.keliling = sisi*4
    def tampilkan(self):
        print("Keliling:",self.keliling,"cm")
        print("Luas:",self.luas,"cm")

persegi1 = Persegi(int(input("Masukkan sisi (cm): ")))
persegi1.tampilkan()
