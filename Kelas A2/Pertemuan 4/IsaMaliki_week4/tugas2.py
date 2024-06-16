class Orang:
    def __init__ (self, nmdp, nmblk, id):
        self.nmdp = nmdp
        self.nmblk = nmblk
        self.id = id

# nomor 7
class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)


# nomor 8
class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)


# nomor 9
class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nmdp, nmblk, id):
        super().__init__(nmdp, nmblk, id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
    
    def cetak(self):
        print(f"Nama = {self.nmdp + " " + self.nmblk}")
        print(f"Nomor ID = {self.id}")
        print(f"Mata Kuliah = {self.matkul}")
        print(f"Mata Kuliah Diajar = {self.matkul_diajar}")
        print("")


# nomor 10
uswatun = Asdos("Uswatun", "Hasanah", 456456)
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")
uswatun.cetak()