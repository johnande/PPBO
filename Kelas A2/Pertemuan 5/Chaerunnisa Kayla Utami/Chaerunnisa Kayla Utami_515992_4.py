class Angka:
    def __init__(self, nilai):
        self.nilai = nilai
    
    def __add__(self, other):
        return self.nilai + other.nilai
    
    def __str__(self):
        return str(self.nilai)

angka1 = Angka(5)
angka2 = Angka(10)
hasil = angka1 + angka2
print("Hasil penjumlahan:", hasil)
