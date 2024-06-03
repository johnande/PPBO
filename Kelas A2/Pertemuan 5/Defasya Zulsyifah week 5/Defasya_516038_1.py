class Tumbuhan:
    def __init__(self, nama):
        self.nama = nama

    def deskripsi(self):
        return "Ini adalah tumbuhan " + self.nama

class TanamanPohon(Tumbuhan):
    def __init__(self, nama, tinggi):
        super().__init__(nama)
        self.tinggi = tinggi

    def deskripsi(self):
        return super().deskripsi() + f" dengan tinggi {self.tinggi} meter."

class TanamanBunga(Tumbuhan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna

    def deskripsi(self):
        return super().deskripsi() + f" dengan warna {self.warna}."

def main():
    pohon = TanamanPohon("Pohon Mangga", 10)
    bunga = TanamanBunga("Mawar", "merah")

    print(pohon.deskripsi())
    print(bunga.deskripsi())

if __name__ == "__main__":
    main()
