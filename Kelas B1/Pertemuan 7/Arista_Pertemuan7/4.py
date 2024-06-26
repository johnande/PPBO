class ResepMakanan:
    def __init__(self, nama):
        self.nama = nama
        self.bahan = []

    def tambah_bahan(self, bahan):
        self.bahan.append(bahan)

    def masak(self):
        print("Resep membuat", self.nama)
        print("Bahan-bahan:")
        for bahan in self.bahan:
            print("- ", bahan)
        print("Langkah-langkah:")
        print("1. Siapkan bahan yang diperlukan.")
        print("2. Tumis bawang aroma tercium.")
        print("3. Masukkan telur, sosis, dan nasi.")
        print("4. Tambahkan kecap manis dan garam.")
        print("5. Masak hingga semua bahan matang.")
        print("6. Sajikan dan nikmati!")

def resep_makanan(nama):
    def decorator_resep(class_):
        class_.nama = nama
        return class_
    return decorator_resep

@resep_makanan("Nasi Goreng")
class NasiGoreng(ResepMakanan):
    def __init__(self):
        super().__init__(self.nama)
        self.tambah_bahan("2 piring nasi")
        self.tambah_bahan("3 siung bawang putih, cincang")
        self.tambah_bahan("2 sdm kecap manis")
        self.tambah_bahan("Garam secukupnya")
        self.tambah_bahan("Minyak goreng")
        self.tambah_bahan("2 butir telur")
        self.tambah_bahan("Sosis  dipotong kecil")

nasi_goreng = NasiGoreng()
nasi_goreng.masak()
