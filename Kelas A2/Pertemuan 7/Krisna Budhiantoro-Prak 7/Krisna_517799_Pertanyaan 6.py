from collections import namedtuple

Mahasiswa = namedtuple("Mahasiswa", ["nama", "usia", "jurusan"])

mahasiswa1 = Mahasiswa("Krisna", 20, "Teknik Informatika")
mahasiswa2 = Mahasiswa("Mahda", 21, "Ilmu Komputer")

print("Informasi Mahasiswa:")
print("Nama:", mahasiswa1.nama)
print("Usia:", mahasiswa1.usia)
print("Jurusan:", mahasiswa1.jurusan)

print("\nInformasi Mahasiswa:")
print("Nama:", mahasiswa2.nama)
print("Usia:", mahasiswa2.usia)
print("Jurusan:", mahasiswa2.jurusan)