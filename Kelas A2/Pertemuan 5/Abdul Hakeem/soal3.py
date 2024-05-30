class barang:
    def __init__(self, merek, hargasatuan):
        self.merek = merek
        self.hargasatuan = hargasatuan # hargasatuan ribu rupiah

    def __mul__(self, quantity):
        print(f"Banyaknya penjualan: {quantity.qtysold} buah")
        return self.hargasatuan * quantity.qtysold
    
class penjualan:
    def __init__(self, merek, qtysold):
        self.merek = merek
        self.qtysold = qtysold

bramble = barang("Bramble", 2140)
qty_march = penjualan("Bramble", 20)

print(f"Total penjualan {bramble.merek}: {bramble * qty_march} ribu")
