class Buku:
    def __init__(self, Judul, Penulis):
        self.Judul = Judul
        self.Penulis = Penulis
    
    def __add__(self, tambah):
        return [self, tambah]

# Contoh penggunaan
buku1 = Buku("Filosofi Teras", "Henry Manampiring")
buku2 = Buku("Rich Dad Poor Dad", "Robert Kiyosaki")

# Penambahan buku
list_buku = buku1 + buku2
for Buku in list_buku:
    print("Judul:", Buku.Judul)
    print("Penulis:", Buku.Penulis)