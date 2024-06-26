class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.absen = False
    
    def absenkan(self):
        self.absen = True
        print(f"{self.nama} telah melakukan absen.")

# Membuat objek karyawan
karyawan1 = Karyawan("Alice", 101)
karyawan2 = Karyawan("Bob", 102)

# Memanggil metode absenkan untuk menampilkan output
karyawan1.absenkan()
karyawan2.absenkan()

