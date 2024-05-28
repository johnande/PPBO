class Pelajar():
    def __init__(self):
        self.matkul=[]

    def enrol(self, matkul):
        self.matkul.append(matkul)

    def tampilkan(self):
        print("===Mata Kuliah Pelajar===")
        print("Mata Kuliah: ", self.matkul)

pelajar1 = Pelajar()
pelajar1.enrol("Basis Data, Matematika")
pelajar1.enrol("Pemrograman Komputer")
pelajar1.tampilkan()