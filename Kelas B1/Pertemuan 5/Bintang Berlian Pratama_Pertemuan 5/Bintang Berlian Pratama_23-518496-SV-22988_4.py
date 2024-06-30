class Buku:
    def __init__(self, judul, halaman):
        self.judul = judul
        self.halaman = halaman
    def __lt__(self, other):
        return self.halaman < other.halaman
    def __gt__(self, other):
        return self.halaman > other.halaman
    def __eq__(self, other):
        return self.halaman == other.halaman

buku1 = Buku("Pemrograman Database Berbasis Web", 200)
buku2 = Buku("Atomic Habits", 340)

if buku1 > buku2:
    print(buku1.judul,"memiliki halaman yang lebih banyak daripada",buku2.judul)
elif buku1 < buku2:
    print(buku1.judul,"memiliki halaman yang lebih sedikit daripada",buku2.judul)
else:
    print(buku1.judul,"memiliki halaman yang sama dengan",buku2.judul)
