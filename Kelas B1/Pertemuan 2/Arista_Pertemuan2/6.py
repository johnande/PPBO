class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

# Input dari pengguna
nama_input = input("Masukkan nama: ")
umur_input = input("Masukkan umur: ")

# Membuat objek Manusia
orang = Manusia(nama_input, umur_input)

# Menampilkan informasi
orang.info()
