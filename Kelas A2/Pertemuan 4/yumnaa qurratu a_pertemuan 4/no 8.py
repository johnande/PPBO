class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)
        print(f"Berhasil menambahkan mata kuliah {matkul} ke dalam daftar mata kuliah yang diajar.")

if __name__ == "__main__":
    pengajar1 = Pengajar()

    pengajar1.mengajar("Basis Data")
    pengajar1.mengajar("Bahasa Inggris")

    print("Daftar Mata Kuliah yang Diajar:")
    print(pengajar1.matkul_diajar)
