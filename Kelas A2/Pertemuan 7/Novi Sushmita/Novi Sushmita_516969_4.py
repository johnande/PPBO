def tambah_keragaman(cls):
    def keragaman(self):
        print(f"Selamat datang di {self.nama_tempat}, tempat yang memperkaya keberagaman Indonesia!")
    cls.keragaman = keragaman
    return cls

@tambah_keragaman
class Tempat:
    def __init__(self, nama_tempat):
        self.nama_tempat = nama_tempat

obj = Tempat("Pulau Bali")

obj.keragaman()