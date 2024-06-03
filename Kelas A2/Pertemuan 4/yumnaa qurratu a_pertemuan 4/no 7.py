class Pelajar:
    def __init__(self):
        self.matkul = [] 
        
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
        print(f"Berhasil mendaftar mata kuliah: {mata_kuliah}")

mahasiswa = Pelajar()
mahasiswa.enrol("PPBO")
mahasiswa.enrol("Bahasa Inggris")

print("Mata kuliah yang diambil:", mahasiswa.matkul)
