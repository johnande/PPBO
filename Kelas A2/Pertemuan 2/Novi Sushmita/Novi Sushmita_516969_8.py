class kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
    def penjumlahan(self):
        return self.angka1 + self.angka2
    def pengurangan(self):
        return self.angka1 - self.angka2
    def perkalian(self):
        return self.angka1 * self.angka2
    def pembagian(self):
        return self.angka1 / self.angka2

#membuat object dengan konstruktor  
kasus1 = kalkulator(4, 2)
#menampilkan menggunakan method
print(kasus1.penjumlahan())
print(kasus1.pengurangan())

kasus2 = kalkulator(30, 6)
print(kasus2.perkalian())
print(kasus2.pembagian())