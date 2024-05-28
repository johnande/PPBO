class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak_informasi(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")

# Input dari pengguna
nama_manusia = input("Masukkan nama: ")
umur_manusia = int(input("Masukkan umur: "))

# Membuat objek Manusia
orang1 = Manusia(nama_manusia, umur_manusia)

# Menampilkan informasi
orang1.cetak_informasi()
