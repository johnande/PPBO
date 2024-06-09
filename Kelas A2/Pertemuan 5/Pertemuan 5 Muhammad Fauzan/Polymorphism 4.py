class Mobil:
    def __init__(self, Name, jenis):
        self.Name = Name
        self.jenis = jenis
    
    def __add__(self, kualitas):
        return self.jenis + kualitas.qty_jual 
    
class Nissan:
    def __init__(self, merek, qty_jual):
        self.merek = merek
        self.qty_jual = qty_jual #harga jual

Skyline = Mobil("Skyline", 1000000)
qty_maret = Nissan("Skyline", 300000)
print(f" {Skyline.jenis} : {Skyline + qty_maret} ")