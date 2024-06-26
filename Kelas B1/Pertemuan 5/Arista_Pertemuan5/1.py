class Sepatu:
    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga

    def deskripsi(self):
        return f"Sepatu {self.merek}"

    def harga_jual(self):
        return self.harga

class SepatuLari:
    def __init__(self, merek, harga, ukuran):
        self.merek = merek
        self.harga = harga
        self.ukuran = ukuran

    def deskripsi(self):
        return f"Sepatu lari {self.merek} ukuran {self.ukuran}"

    def harga_jual(self):
        return self.harga * 1.1  

class SepatuFutsal:
    def __init__(self, merek, harga, warna):
        self.merek = merek
        self.harga = harga
        self.warna = warna

    def deskripsi(self):
        return f"Sepatu futsal {self.merek} warna {self.warna}"

    def harga_jual(self):
        return self.harga * 1.2  

sepatu_olahraga = Sepatu("Nike", 500000)
sepatu_lari = SepatuLari("Adidas", 700000, 42)
sepatu_futsal = SepatuFutsal("Puma", 600000, "biru")

print(sepatu_olahraga.deskripsi(), "- Harga Jual:", sepatu_olahraga.harga_jual())
print(sepatu_lari.deskripsi(), "- Harga Jual:", sepatu_lari.harga_jual())
print(sepatu_futsal.deskripsi(), "- Harga Jual:", sepatu_futsal.harga_jual())
