class Barang:
    def __init__(self, merek, harga_satuan) -> None:
        self.merek = merek
        self.harga_satuan = harga_satuan #dlm ribuan

    def __mul__(self, kuantitas):
        print("banyaknya penjualan:", kuantitas.qty_jual, 'buah')
        return self.harga_satuan * kuantitas.qty_jual
    
class Penjualan:
    def __init__(self, merek, qty_jual) -> None:
        self.merek = merek
        self.qty_jual = qty_jual

redmi10 = Barang('Redmi 10', 2500)
qty_maret = Penjualan('redmi10', 20)
print(f"total penjualan {redmi10.merek}: {redmi10 * qty_maret} ribu")

oppo = Barang('oppo', 3000)
qty_april = Penjualan('oppo', 30)
print(f"total penjualan {oppo.merek}: {oppo * qty_april} ribu")