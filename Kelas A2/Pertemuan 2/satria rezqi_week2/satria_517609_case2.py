class persegi:

    def __init__(self, sisi) -> None:
        self.sisi = sisi

    def luas(self):
        return f'luas persegi dengan panjang sisi {self.sisi} adalah {self.sisi * self.sisi}'
    
    def keliling(self):
        return f'keliling persegi dengan panjang sisi {self.sisi} adalah {4 * self.sisi}'
    
persegi1 = (persegi(4)) 

print(persegi1.luas())
print(persegi1.keliling())


