class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

orang = Manusia("Alice", 30)

# Menghapus atribut umur
del orang.umur

print("Nama: ", orang.nama)

# Menghapus objek manusia
del orang

# Mencoba mengakses objek setelah dihapus akan menghasilkan error
try:
    print(orang.nama)
except NameError as e:
    print("Error:", e)
