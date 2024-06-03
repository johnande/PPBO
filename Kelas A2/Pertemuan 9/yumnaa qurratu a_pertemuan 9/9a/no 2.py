class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
    
    @classmethod
    def dari_dict(cls, info_buku):
        return cls(info_buku['judul'], info_buku['pengarang'])
    
    @staticmethod
    def populer(jumlah_penilaian):
        return jumlah_penilaian >= 10000
    
    @property
    def deskripsi(self):
        return f"{self.judul} oleh {self.pengarang}"

info_buku = {'judul': 'Hujan', 'pengarang': 'Tereliye'}
buku = Buku.dari_dict(info_buku)
print(buku.judul)  # Output: Hujan
print(buku.pengarang)  # Output: Tereliye

jumlah_penilaian = 12000
print(Buku.populer(jumlah_penilaian))  # Output: True

buku_digital = Buku("Bumi", "Tereliye")
print(buku_digital.deskripsi)  # Output: Bumi oleh Tereliye

