class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

pelajar1 = Pelajar()
pelajar1.enrol("Matematika")
pelajar1.enrol("Bahasa Inggris")

print("Mata Kuliah yang Diambil Pelajar:")
print(pelajar1.matkul)
