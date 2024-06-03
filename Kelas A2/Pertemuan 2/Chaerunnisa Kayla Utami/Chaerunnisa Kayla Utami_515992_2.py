# Mendefinisikan sebuah kelas bernama 'Kucing'
class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def suara(self):
        return "Meong!"

# Membuat objek dari kelas 'Kucing'
kucing1 = Kucing("Tom", 3)
kucing2 = Kucing("Jerry", 2)

# Mengakses atribut dan metode dari objek
print(f"{kucing1.nama} berusia {kucing1.umur} tahun dan bersuara {kucing1.suara()}")
print(f"{kucing2.nama} berusia {kucing2.umur} tahun dan bersuara {kucing2.suara()}")