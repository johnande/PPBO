class Mobil:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna
    
    def info(self):
        print("Merk:", self.merk)
        print("Tahun:", self.tahun)
        print("Warna:", self.warna)

# Membuat objek baru dari kelas Mobil dengan konstruktor
mobil1 = Mobil("Toyota Avanza", 2019, "Silver")

# Memanggil method info() dari objek
mobil1.info()

