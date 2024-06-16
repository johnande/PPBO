# nomor 1
class Orang:
    def __init__ (self, nmdp, nmblk, id):
        self.nmdp = nmdp
        self.nmblk = nmblk
        self.id = id


# nomor 2
class Mahasiswa(Orang):
    sarjana = "SARJANA"
    master = "MASTER"
    doktor = "DOKTOR"

    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

    def cetak(self):
        print(f"Nama = {self.nmdp + " " + self.nmblk}")
        print(f"Nomor ID = {self.id}")
        print(f"Jenjang = {self.jenjang}")
        print(f"Mata Kuliah = {self.matkul}")
        print("")


# nomor 3
class Karyawan(Orang):
    tetap = "TETAP"
    tdk_tetap = "TIDAK TETAP"

    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = status

    def cetak(self):
        print(f"Nama = {self.nmdp + " " + self.nmblk}")
        print(f"Nomor ID = {self.id}")
        print(f"Status Karyawan = {self.status}")
        print("")

# nomor 4
class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []
        
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
    
    def cetak(self):
        print(f"Nama = {self.nmdp + " " + self.nmblk}")
        print(f"Nomor ID = {self.id}")
        print(f"Status Karyawan = {self.status}")
        print(f"Mata Kuliah yang Diajar = {self.matkul_diajar}")
        print("")


# nomor 5
bowo = Mahasiswa(Mahasiswa.sarjana, "Bowo", "Nugroho", 987654)
bowo.enrol("Basis Data")
bowo.cetak()

# nomor 6
rizki = Dosen(Dosen.tetap, "Rizki", "Setiabudi", 456789)
rizki.mengajar("Statistik")
rizki.cetak()


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