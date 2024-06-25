class Kucing :
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur
    
    def info(self):
        print(f"Aku adalah kucing, Namaku adalah {self.nama}. Aku berumur {self.umur} tahun.")

    def suara(self):
        print("meong")

class Anjing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"Aku adalah anjing. Namaku adalah {self.nama}. Aku berumur {self.umur} tahun.")

    def suara(self):
        print("Gukguk")

kucing1 = Kucing("Doku", 1.5)
anjing1 = Anjing("Joko", 5)

for hewan in (kucing1, anjing1):
    hewan.suara()
    hewan.info()
    hewan.suara()