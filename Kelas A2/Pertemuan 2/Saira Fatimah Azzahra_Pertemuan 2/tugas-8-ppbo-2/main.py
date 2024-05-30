class Tanaman:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def info_tanaman(self):
        print("Nama Tanaman:", self.nama)
        print("Jenis Tanaman:", self.jenis)

# Membuat objek-objek Tanaman
tanaman1 = Tanaman("Mawar", "Dikotil")
tanaman2 = Tanaman("Padi", "Monokotil")

# Menampilkan informasi tentang tanaman-tanaman
print("Informasi Tanaman 1:")
tanaman1.info_tanaman()
print("\nInformasi Tanaman 2:")
tanaman2.info_tanaman()
