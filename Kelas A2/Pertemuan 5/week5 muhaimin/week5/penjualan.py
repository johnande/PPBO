class Barang:
    def __init__(self,merk,harga_satuan):
        self.merk= merk
        self.harga_satuan= harga_satuan
    
    def __mul__(self,kuantitas):
        print("Banyaknya penjualan", kuantitas.qty_jual,"buah")
        return self.harga_satuan * kuantitas.qty_jual
        
class Penjualan:
    def __init__(self,merk,qty_jual):
        self.merk= merk
        self.qty_jual= qty_jual

redmi10= Barang("redmi10",2140)
qty_maret= Penjualan("redmi10",20)
print(f"Total penjualan {redmi10.merk}: {redmi10*qty_maret} ribu")