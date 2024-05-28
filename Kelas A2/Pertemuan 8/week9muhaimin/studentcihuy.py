from collections import namedtuple

# Membuat namedtuple Student
Student = namedtuple("Student", ["nama", "nim", "jurusan"])

# Membuat daftar mahasiswa
mahasiswa = [
    Student("John Doe", "123456", "Informatika"),
    Student("Jane Smith", "654321", "Teknik Elektro"),
    Student("Bob Johnson", "987654", "Sistem Informasi")
]

# Menampilkan informasi mahasiswa
for mhs in mahasiswa:
    print("Nama:", mhs.nama)
    print("NIM:", mhs.nim)
    print("Jurusan:", mhs.jurusan)
    print()
