class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def display_info(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_semua_buku(self):
        print("Daftar Buku:")
        for buku in self.daftar_buku:
            buku.display_info()

# Membuat objek buku
buku1 = Buku("Harry Potter", "J.K. Rowling", 1997)
buku2 = Buku("Lord of the Rings", "J.R.R. Tolkien", 1954)

# Membuat objek perpustakaan
perpustakaan = Perpustakaan()

# Menambahkan buku ke dalam perpustakaan
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)

# Menampilkan semua buku dalam perpustakaan
perpustakaan.tampilkan_semua_buku()
