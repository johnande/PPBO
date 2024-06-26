class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        Orang.__init__(self, nama_depan, nama_belakang, nomor_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

asdos1 = Asdos("Ani", "Laras", "96874")
asdos1.enrol("Pemrograman")
asdos1.mengajar("Inggris")

print("Nama:", asdos1.nama_depan, asdos1.nama_belakang)
print("Nomor ID:", asdos1.nomor_id)
print("Mata kuliah yang diambil:", asdos1.matkul)
print("Mata kuliah yang diajar:", asdos1.matkul_diajar)


