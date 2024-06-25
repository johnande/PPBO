#No6

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_info(self):
        print(f"Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun.")

nama_input = input("Masukkan nama Anda: ")
umur_input = int(input("Masukkan umur Anda: "))

orang = Manusia(nama_input, umur_input)
orang.cetak_info()