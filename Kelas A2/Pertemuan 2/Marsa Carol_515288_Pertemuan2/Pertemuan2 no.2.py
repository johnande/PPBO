class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

# Membuat objek dari kelas 'Mahasiswa'
mhs1 = Mahasiswa("Marsa", "12345", "TRI")
mhs2 = Mahasiswa("Carol", "54321", "TRPL")

# Menampilkan informasi mahasiswa
print(f"Informasi Mahasiswa:\nNama: {mhs1.nama}, NIM: {mhs1.nim}, Jurusan: {mhs1.jurusan}")
print(f"Informasi Mahasiswa:\nNama: {mhs2.nama}, NIM: {mhs2.nim}, Jurusan: {mhs2.jurusan}")

