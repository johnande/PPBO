#No6 soal3_Menghapus Atribut

class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

mobil_saya = Mobil("Toyota", 2020)
print("Merk sebelum dihapus:", mobil_saya.merk)

delattr(mobil_saya, "merk")
print("Merk setelah dihapus:", mobil_saya.merk)
