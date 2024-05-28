class persegi:
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi ** 2
    def keliling(self):
        return self.sisi * 4
    def tampilkan(self):
        print("Luas persegi : " + str(self.luas()))
        print("Keliling persegi : " + str(self.keliling()))

persegi1 = persegi(6)
persegi1.tampilkan()

persegi2 = persegi(9)
persegi2.tampilkan()