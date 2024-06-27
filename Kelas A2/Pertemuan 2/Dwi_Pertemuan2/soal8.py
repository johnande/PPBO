class siswa:
    def __init__ (self, Nama, Kelas, Angkatan):
        self.Nama = Nama
        self.Kelas = Kelas
        self.Angkatan = Angkatan
    def tampilkan_data(self):
        print("Nama : " + self.Nama)
        print("Kelas : " + str(self.Kelas))
        print("Angkatan : " + str(self.Angkatan))

siswa1 = siswa("Bagas", 12, 2020)
siswa1.tampilkan_data()
