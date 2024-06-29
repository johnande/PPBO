class persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    
    def keliling(self):
        return self.sisi * 4
        
    def luas(self):
        return self.sisi * self.sisi

persegi1 = persegi(10)

print("Kelliling persegi:", persegi1.keliling(), 
"\nLuas persegi:", persegi1.luas())