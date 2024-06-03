class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID

    def info(self):
        print("Nama:", self.nama_depan, self.nama_belakang)
        print("Nomor ID:", self.nomor_ID)

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
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        Orang.__init__(self, nama_depan, nama_belakang, nomor_ID)
        Pelajar.__init__(self)
        Pengajar.__init__(self)


uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

uswatun.info()
uswatun.info_pelajar()
uswatun.info_pengajar()
