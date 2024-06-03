class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")

nama_input = input("Masukkan nama: ")
umur_input = input("Masukkan umur: ")

orang = Manusia(nama_input, umur_input)

orang.cetak_info()
