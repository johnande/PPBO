class sayur:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def tampil(self):
        print(f"Nama sayur: {self.nama}")
        print(f"Warna sayur: {self.warna}")

sayur1 = sayur("Kangkung", "Hijau")
sayur2 = sayur("Tomat", "Merah")

sayur1.tampil()
sayur2.tampil()