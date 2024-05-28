class Receipt:
    total_pembelian = 0

    def __init__(self, nama, tanggal_pembelian):
        self.nama = nama
        self.tanggal_pembelian = tanggal_pembelian

    @classmethod
    def tambah_harga_barang(cls, harga_barang):
        cls.total_pembelian += harga_barang
        return cls.total_pembelian
    
    @staticmethod
    def kurang_harga_barang(harga_barang):
        Receipt.total_pembelian -= harga_barang
        return Receipt.total_pembelian
    
    @property
    def points(self):
        return self.total_pembelian // 10000

# membuat objek
andi = Receipt("John Doe", "29-04-2024")

# memanggil method yang menggunakan @classmethod
total_setelah_tambah = Receipt.tambah_harga_barang(20000)
print("Total setelah ditambah :", total_setelah_tambah)

# memanggil method yang menggunakan @staticmethod
total_setelah_kurang = Receipt.kurang_harga_barang(10000)
print("Total setelah dikurang :", total_setelah_kurang)

print("\n=== Receipt ===")
print("Nama : ", andi.nama)
print("Tanggal : ", andi.tanggal_pembelian)
print("Total : ", andi.total_pembelian)
# memanggil method yang menggunakan @property
print("Points : ", andi.points)