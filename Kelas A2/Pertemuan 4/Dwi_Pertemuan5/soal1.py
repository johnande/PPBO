class Ayam:
    def jenis_hewan(self):
        print("Unggas")
    def jumlah_kaki(self):
        print("Ayam berkaki dua")

class Sapi:
    def jenis_hewan(self):
        print("Mamalia")
    def jumlah_kaki(self):
        print("Sapi berkaki empat")

ayam = Ayam()
sapi = Sapi()
for hewan in (ayam, sapi):
    hewan.jenis_hewan()
    hewan.jumlah_kaki()