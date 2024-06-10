class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

pelajar1 = Pelajar()
pelajar1.enrol("SOJ")
pelajar1.enrol("PBO")

print("Mata kuliah yang diambil:", ', '.join(pelajar1.matkul))

