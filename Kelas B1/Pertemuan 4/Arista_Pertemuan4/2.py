class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_ID = nomer_ID

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        Orang.__init__(self, nama_depan, nama_belakang, nomer_ID)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

print(f"Asdos: {uswatun.nama_depan} {uswatun.nama_belakang}, Nomor ID: {uswatun.nomer_ID}")
print(f"Mata kuliah yang diambil: {uswatun.matkul}")
print(f"Mata kuliah yang diajar: {uswatun.matkul_diajar}")
