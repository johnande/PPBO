from collections import namedtuple

Karyawan = namedtuple("Karyawan", ["nama", "usia", "departemen"])

Karyawan1 = Karyawan("Budi Tabudi", 35, "Marketing")
Karyawan2 = Karyawan("Arya Putra", 23, "Akuntansi")

print("Data Karyawan 1:")
print("Nama:", Karyawan1.nama)
print("Usia:", Karyawan1.usia)
print("Departemen:", Karyawan1.departemen)
print("\nData Karyawan 2:")
print("Nama:", Karyawan2.nama)
print("Usia:", Karyawan2.usia)
print("Departemen:", Karyawan2.departemen)