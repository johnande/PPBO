class Pengajar:
    def __init__(self):
        self.matkul_diajar = []
        
    def enrol(self, matkul):
        self.matkul_diajar.append(matkul)
        
pengajar = Pengajar()
pengajar.enrol("Bahasa Inggris")
pengajar.enrol("Bahasa Indonesia")
print("Pengajar Mata Kuliah:", pengajar.matkul_diajar)