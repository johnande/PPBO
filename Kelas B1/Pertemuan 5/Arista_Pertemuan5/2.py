class Buah:
    def __init__(self, nama):
        self.nama = nama

    def cara_makan(self):
        pass

class Apel(Buah):
    def cara_makan(self):
        return "Apel bisa dimakan langsung atau dibuat jus."

class Pisang(Buah):
    def cara_makan(self):
        return "Pisang enak dimakan mentah atau dibuat kolak."

class Jeruk(Buah):
    def cara_makan(self):
        return "Jeruk segar saat diperas menjadi jus."

def buat_sup_buah(buah):
    print(f"Sup buah dari {buah.nama}: {buah.cara_makan()}")

apel = Apel("Apel hijau")
pisang = Pisang("Pisang kepok")
jeruk = Jeruk("Jeruk sunkist")

buat_sup_buah(apel)
buat_sup_buah(pisang)
buat_sup_buah(jeruk)
