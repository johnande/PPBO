class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

# Contoh penggunaan
pengajar1 = Pengajar()
pengajar1.mengajar("Fisika")
pengajar1.mengajar("Kimia")

print("Mata Kuliah yang Diajar Pengajar:")
print(pengajar1.matkul_diajar)
