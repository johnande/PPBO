class Persegi:
    def __init__(self,Sisi):
        self.sisi = Sisi

    def Luas(self):
        LuasP = self.sisi ** 2
        print("Luas Persegi:", LuasP)

    def Keliling(self):
        KelilingP = self.sisi * 4
        print("Keliling Persegi:", KelilingP)

persegi1 = Persegi(5)

persegi1.Luas()
persegi1.Keliling()