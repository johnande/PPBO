class Orang :
    def __init__(self, nama_depan, nama_belakang, nomor_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

#Nomor 7
class Pelajar :
    def __init__(self):
        self.matkul = []
    def enrol(self, matkul):
        self.matkul.append(matkul)

# Nomor 8
class Pengajar :
    def __init__(self, *args, **kwargs):
        self.matkul_diajar = []
    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

#Nomor 9
class Asdos (Orang, Pelajar, Pengajar):
    def __init__(self, *args, **kwargs):
        Orang.__init__(self, *args, **kwargs)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

#Nomor 10
uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")