class Bunga:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def mekar(self):
        print(f"{self.nama} mekar dengan warna {self.warna}")

# Membuat objek dari kelas Bunga
mawar = Bunga(nama="Mawar", warna="Merah")

# Mengakses atribut objek
print(f"Nama: {mawar.nama}")
print(f"Warna: {mawar.warna}")

# Memanggil metode pada objek
mawar.mekar()

