from collections import namedtuple

Mahasiswa = namedtuple('Mahasiswa', ['nama', 'umur', 'jurusan'])

mahasiswa1 = Mahasiswa(nama='John', umur=20, jurusan='Informatika')
mahasiswa2 = Mahasiswa(nama='Jane', umur=21, jurusan='Manajemen')

print("Data Mahasiswa 1:")
print("Nama:", mahasiswa1.nama)
print("Umur:", mahasiswa1.umur)
print("Jurusan:", mahasiswa1.jurusan)

print("\nData Mahasiswa 2:")
print("Nama:", mahasiswa2.nama)
print("Umur:", mahasiswa2.umur)
print("Jurusan:", mahasiswa2.jurusan)
