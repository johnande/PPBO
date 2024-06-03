
# Nomor 7: Membuat Kelas Dengan Nama Pelajar
class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

# Nomor 8: Membuat Kelas Dengan Nama Pengajar
class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

# Nomor 9: Membuat Kelas Dengan Nama Asdos
class Asdos(Pelajar, Pengajar):
    pass

uswatun = Asdos()

# Nomor 10: Membuat Objek dengan Nama Uswatun Menggunakan Kelas Asdos
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

