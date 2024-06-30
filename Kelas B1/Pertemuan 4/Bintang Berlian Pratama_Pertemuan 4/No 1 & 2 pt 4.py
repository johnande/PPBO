class Orang:
    def __init__(self, namadepan, namabelakang, nomerID):
        self.namadepan = namadepan
        self.namabelakang = namabelakang
        self.nomerID = nomerID
        self.matkul = []
        self.matkul_diajar = []

class Mahasiswa(Orang):
    SARJANA, MASTER, DOKTOR = range(3)
    def __init__(self, namadepan, namabelakang, nomerID, jenjang):
        super().__init__(namadepan, namabelakang, nomerID)
        self.jenjang = jenjang
        self.matkul = []
    def enroll(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)
    def __init__(self, namadepan, namabelakang, nomerID, status):
        super().__init__(namadepan, namabelakang, nomerID)
        self.status = status

class Dosen(Karyawan):
    def __init__(self, namadepan, namabelakang, nomerID, status):
        super().__init__(namadepan, namabelakang, nomerID, status)
        self.matkul_diajar = []
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

bowo = Mahasiswa("Bowo","Nugroho",987654,Mahasiswa.SARJANA)
bowo.enroll("Basis Data")

print("Informasi tentang bowo:")
print("Nama:", bowo.namadepan, bowo.namabelakang)
print("Nomor ID:", bowo.nomerID)
print("Jenjang:", bowo.jenjang)
print("Mata kuliah yang diambil:", bowo.matkul)

rizki = Dosen("Rizki","Setiabudi",456789,Karyawan.TETAP)
rizki.mengajar("Statistik")

print("\nInformasi tentang rizki:")
print("Nama:", rizki.namadepan, rizki.namabelakang)
print("Nomor ID:", rizki.nomerID)
print("Status Karyawan:", rizki.status)
print("Mata kuliah yang diajar:", rizki.matkul_diajar)

class Pelajar:
    def __init__(self):
        self.matkul = []
    def enroll(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, namadepan, namabelakang, nomerID):
        super().__init__(namadepan, namabelakang, nomerID)

uswatun = Asdos("Uswatun","Hasanah",456456)
uswatun.enroll("Big Data")
uswatun.mengajar("Kecerdasan Artificial")

print("\nInformasi tentang uswatun:")
print("Nama:", uswatun.namadepan, uswatun.namabelakang)
print("Nomor ID:", uswatun.nomerID)
print("Mata kuliah yang diambil:", uswatun.matkul)
print("Mata kuliah yang diajar:", uswatun.matkul_diajar)