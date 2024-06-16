class persegi:
    def __init__(self, s):
        self.sisi = s
    
    def hitung_luas(self):
        return self.sisi**2

    def hitung_keliling(self):
        return self.sisi*4
    
    def cetak(self):
        luas = self.hitung_luas()
        keliling = self.hitung_keliling()
        print(f'Luas Persegi adalah {luas}')
        print(f'Keliling Persegi adalah {keliling}')


persegi1 = persegi(5)

persegi1.cetak()
