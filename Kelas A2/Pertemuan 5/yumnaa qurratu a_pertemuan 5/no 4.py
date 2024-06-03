class Bunga:
    def __init__(self, nama, warna, harga_per_tangkai):
        self.nama = nama
        self.warna = warna
        self.harga_per_tangkai = harga_per_tangkai  # dalam ribu

    def __mul__(self, jumlah):
        print('Jumlah pembelian:', jumlah)
        return self.harga_per_tangkai * jumlah

class Warna:
    def __init__(self, nama):
        self.nama = nama

mawar = Bunga("Mawar", Warna("Merah"), 2000)

total_biaya = mawar * 12

print(f"Total biaya untuk {mawar.warna.nama} {mawar.nama}: {total_biaya} ribu")
