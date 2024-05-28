class Orang:
    def __init__(self, namdep, nambel, nomor_id):
        self.namdep = namdep
        self.nambel = nambel
        self.nomor_id = nomor_id

class Pelajar():
    def __init__(self):
        self.matkul=[]

    def enrol(self, matkul):
        self.matkul.append(matkul)

class Pengajar():
    def __init__(self):
        self.matkul_diajar=[]

    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, namdep, nambel, nomor_id):
        super().__init__(namdep, nambel, nomor_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
    
    def tampilkan(self):
        print("===Asdos===")
        print("Nama: ", self.namdep, self.nambel)
        print("Nomor ID: ", self.nomor_id)
        print("Mata Kuliah: ", self.matkul)
        print("Mata Kuliah Diajar: ", self.matkul_diajar)

asdos1 = Asdos("Novi", "Sushmita", 9)
asdos1.enrol("Teknik Telekomunikasi")
asdos1.mengajar("Praktikum Teknik Telekomunikasi")
asdos1.tampilkan()