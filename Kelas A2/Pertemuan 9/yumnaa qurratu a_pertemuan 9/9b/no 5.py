from collections import namedtuple

Buku = namedtuple('Buku', ['judul', 'pengarang', 'tahun_terbit'])

def buat_buku(judul, pengarang, tahun_terbit):
    return Buku(judul=judul, pengarang=pengarang, tahun_terbit=tahun_terbit)

daftar_buku = []

daftar_buku.append(buat_buku('Hujan', 'Tere Liye', 2016))
daftar_buku.append(buat_buku('Negeri Para Bedebah', 'Tere Liye', 2012))
daftar_buku.append(buat_buku('Negeri 5 Menara', 'Ahmad Fuadiyang', 2009))

print("Daftar Buku dalam Perpustakaan:")
for buku in daftar_buku:
    print(f"Judul: {buku.judul}, Pengarang: {buku.pengarang}, Tahun Terbit: {buku.tahun_terbit}")
