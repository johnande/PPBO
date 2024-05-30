class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

# Masukan inputan :
sisi = float(input("Masukan panjang sisi persegi: "))
persegi = Persegi(sisi)
print("Luas persegi =", persegi.luas())
print("Keliling persegi =", persegi.keliling())