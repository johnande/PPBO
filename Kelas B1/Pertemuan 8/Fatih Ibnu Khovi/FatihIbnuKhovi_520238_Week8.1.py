class Konversi:
    def __init__(self, mil):
        self.mil = mil
    
    def kilometer(self):
        return self.mil * 1.60934

Angka = (float(input("Masukan angka dalam satuan mil: ")))
Konversi1 = Konversi(Angka)
print(Angka," mil =", Konversi1.kilometer(),"kilometer.")