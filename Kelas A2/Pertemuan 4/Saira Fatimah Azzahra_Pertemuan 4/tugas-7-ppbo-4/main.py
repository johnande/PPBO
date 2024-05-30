class Pelajar:
    def __init__(self):
        self.matkul = []
        
    def enrol(self, matkul):
        self.matkul.append(matkul)
        
pelajar = Pelajar()
pelajar.enrol("Bahasa Inggris")
pelajar.enrol("Bahasa Indonesia")
print("Mata Kuliah yang Diambil adalah", pelajar.matkul)