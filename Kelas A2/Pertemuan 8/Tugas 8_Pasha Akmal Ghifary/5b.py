from collections import namedtuple

Mahasiswa = namedtuple("Mahasiswa", ["nama", "nim", "jurusan"])

mahasiswa1 = Mahasiswa(nama="John Doe", nim="123456", jurusan="Informatika")
mahasiswa2 = Mahasiswa(nama="Jane Smith", nim="654321", jurusan="Sistem Informasi")

print("Informasi Mahasiswa 1:")
print("Nama:", mahasiswa1.nama)
print("NIM:", mahasiswa1.nim)
print("Jurusan:", mahasiswa1.jurusan)

print("\nInformasi Mahasiswa 2:")
print("Nama:", mahasiswa2.nama)
print("NIM:", mahasiswa2.nim)
print("Jurusan:", mahasiswa2.jurusan)
