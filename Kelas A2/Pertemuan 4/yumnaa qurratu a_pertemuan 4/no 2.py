class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_ID = nomer_ID

class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"
    def __init__(self, nama_depan, nama_belakang, nomer_ID, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_ID)
        self.jenjang = jenjang
        self.matkul = []
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

mahasiswa1 = Mahasiswa("Yumnaa", "Qurratu Ainii", "515239", Mahasiswa.SARJANA)
mahasiswa1.enrol("Inggris")
mahasiswa1.enrol("Teknik Telekomunikasi")
mahasiswa1.enrol("PPBO")

print(f"Nama: {mahasiswa1.nama_depan} {mahasiswa1.nama_belakang}")
print(f"Nomer ID: {mahasiswa1.nomer_ID}")
print(f"Jenjang: {mahasiswa1.jenjang}")
print("Mata Kuliah yang diambil:")
for mata_kuliah in mahasiswa1.matkul:
    print(mata_kuliah)

