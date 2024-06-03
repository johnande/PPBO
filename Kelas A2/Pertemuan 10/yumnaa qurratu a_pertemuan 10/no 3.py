class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang

    def __str__(self):
        return f"{self.judul} oleh {self.pengarang}"

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_daftar_buku(self):  
        for buku in self.daftar_buku:
            print(buku)

class PabrikPerpustakaan:
    @staticmethod
    def buat_perpustakaan():
        return Perpustakaan()

pabrik_perpustakaan = PabrikPerpustakaan()
perpustakaan = pabrik_perpustakaan.buat_perpustakaan()

buku1 = Buku("Hujan", "Tere Liye")
buku2 = Buku("Laut Bercerita", "Leila Salikha Chudori")
buku3 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")

perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tambah_buku(buku3)

print("Daftar Buku di Perpustakaan:")
perpustakaan.tampilkan_daftar_buku() 
