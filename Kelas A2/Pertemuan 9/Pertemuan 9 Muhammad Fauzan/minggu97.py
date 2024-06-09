from collections import namedtuple

# Mendefinisikan namedtuple Mahasiswa
Mahasiswa = namedtuple("Mahasiswa", ["nama", "nim", "jurusan", "ipk"])

# Membuat beberapa instance Mahasiswa
mahasiswa1 = Mahasiswa("Uzi", "987123456", "Teknik Informatika", "4.0")
mahasiswa2 = Mahasiswa("Uzan", "456987321", "TRI", "4.0")
mahasiswa3 = Mahasiswa("Adiz", "231654897", "Biologi", "4.0" )

# Mengakses atribut-atribut namedtuple
print("Nama mahasiswa 1:", mahasiswa1.nama)
print("NIM mahasiswa 1:", mahasiswa1.nim)
print("Jurusan mahasiswa 1:", mahasiswa1.jurusan)
print("ipk mahasiswa 1:", mahasiswa1.ipk)

print("Nama mahasiswa 2:", mahasiswa2.nama)
print("NIM mahasiswa 2:", mahasiswa2.nim)
print("Jurusan mahasiswa 2:", mahasiswa2.jurusan)
print("ipk mahasiswa 2:", mahasiswa2.ipk)

print("Nama mahasiswa 3:", mahasiswa3.nama)
print("NIM mahasiswa 3:", mahasiswa3.nim)
print("Jurusan mahasiswa 3:", mahasiswa3.jurusan)
print("ipk mahasiswa 3:", mahasiswa3.ipk)