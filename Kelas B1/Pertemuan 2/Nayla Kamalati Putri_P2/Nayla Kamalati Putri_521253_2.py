#No2

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

produk1 = Produk('kuaci', 500)

produk2 = Produk('kacang', 300)

print(f"Produk 1: {produk1.nama} (harga: {produk1.harga} rupiah)")
print(f"Produk 2: {produk2.nama} (harga: {produk2.harga} rupiah)")