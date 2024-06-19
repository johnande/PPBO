class Manusia:
    def __init__(self, nama, umur):  # Fixed the method name from '_init_' to '__init__'
        self.nama = nama
        self.umur = umur

    def tampilkan_data(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")

nama_input = input("Masukkan nama: ")
umur_input = input("Masukkan umur: ")

orang = Manusia(nama_input, umur_input)

orang.tampilkan_data()
