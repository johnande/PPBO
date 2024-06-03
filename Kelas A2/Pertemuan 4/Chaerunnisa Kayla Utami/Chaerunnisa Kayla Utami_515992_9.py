class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)


class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

    def info_pelajar(self):
        print("Mata Kuliah yang Diambil Pelajar:")
        print(self.matkul)


class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

    def info_pengajar(self):
        print("Mata Kuliah yang Diajar Pengajar:")
        print(self.matkul_diajar)


class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama, umur):
        Orang.__init__(self, nama, umur)
        Pelajar.__init__(self)
        Pengajar.__init__(self)


# Contoh penggunaan
asdos1 = Asdos("Ali", 20)
asdos1.enrol("Matematika")
asdos1.mengajar("Fisika")

# Memanggil method info dari masing-masing parent class
asdos1.info()
asdos1.info_pelajar()
asdos1.info_pengajar()
