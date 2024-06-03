class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_ID = nomer_ID

class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"
    
    def __init__(self, nama_depan, nama_belakang, nomer_ID, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_ID)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

# Contoh penggunaan
mahasiswa1 = Mahasiswa("John", "Doe", "12345", Mahasiswa.SARJANA)
print("Nama:", mahasiswa1.nama_depan, mahasiswa1.nama_belakang)
print("Nomer ID:", mahasiswa1.nomer_ID)
print("Jenjang:", mahasiswa1.jenjang)

mahasiswa1.enrol("Matematika")
mahasiswa1.enrol("Fisika")
print("Mata kuliah yang diambil:", mahasiswa1.matkul)
