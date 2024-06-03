class Makanan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

# Membuat objek makanan
nasi_goreng = Makanan("Nasi Goreng", 15000)

# Menampilkan atribut sebelum dihapus
print("Atribut sebelum dihapus:")
print("Nama:", nasi_goreng.nama)
print("Harga:", nasi_goreng.harga)

# Menghapus objek makanan
del nasi_goreng

# Mencoba mengakses objek makanan setelah dihapus
try:
    print("\nCoba akses objek makanan setelah dihapus:", nasi_goreng)
except NameError:
    print("Objek 'nasi_goreng' telah dihapus")

