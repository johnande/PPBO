from collections import namedtuple

# Mendefinisikan namedtuple 'Mahasiswa' dengan atribut 'nama', 'nim', dan 'jurusan'
Mahasiswa = namedtuple('Mahasiswa', ['nama', 'nim', 'jurusan'])

# Membuat instance dari namedtuple 'Mahasiswa'
mahasiswa1 = Mahasiswa('Budi', '12345', 'Teknik Informatika')
mahasiswa2 = Mahasiswa('Ani', '67890', 'Ekonomi')

# Mengakses atribut namedtuple dengan cara yang mudah dibaca
print(f"Nama mahasiswa 1: {mahasiswa1.nama}")
print(f"NIM mahasiswa 2: {mahasiswa2.nim}")
print(f"Jurusan mahasiswa 1: {mahasiswa1.jurusan}")
