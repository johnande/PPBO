class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        luas = self.sisi ** 2
        return luas

    def hitung_keliling(self):
        keliling = 4 * self.sisi
        return keliling
    
persegi = Persegi(5)

luas = persegi.hitung_luas()
print("Luas Persegi:", luas)

keliling = persegi.hitung_keliling()
print("Keliling Persegi:", keliling)
