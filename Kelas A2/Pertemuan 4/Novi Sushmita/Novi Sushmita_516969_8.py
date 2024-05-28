class Pengajar():
    def __init__(self):
        self.matkul_diajar=[]

    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

    def tampilkan(self):
        print("===Mata Kuliah Pengajar===")
        print("Mata Kuliah: ", self.matkul_diajar)

pengajar1 = Pengajar()
pengajar1.mengajar("Ilmu Komunikasi, Bahasa Korea")
pengajar1.mengajar("Pemrograman Komputer")
pengajar1.tampilkan()