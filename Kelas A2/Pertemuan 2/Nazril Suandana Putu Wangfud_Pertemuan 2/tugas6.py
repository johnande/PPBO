class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)

# Masukan inputan:
nama = input("Masukan nama: ")
umur = int(input("Masukan umur: "))
manusia = Manusia(nama, umur)
manusia.cetak_info()