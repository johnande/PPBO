from collections import namedtuple

# Membuat namedtuple untuk merepresentasikan informasi pengguna
Pengguna = namedtuple("Pengguna", ["nama", "email", "alamat"])

# Fungsi untuk mendapatkan input pengguna dan membuat instance Pengguna
def input_pengguna():
    nama = input("Masukkan nama Anda: ")
    email = input("Masukkan email Anda: ")
    alamat = input("Masukkan alamat Anda: ")
    return Pengguna(nama=nama, email=email, alamat=alamat)

# Inisialisasi data pengguna
pengguna1 = input_pengguna()

# Menampilkan informasi pengguna
print("\nInformasi Pengguna:")
print("Nama:", pengguna1.nama)
print("Email:", pengguna1.email)
print("Alamat:", pengguna1.alamat)
