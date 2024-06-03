class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        
class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"
    
    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.jenjang = jenjang
        self.matkul = []
        
    def enrol(self, matkul):
        self.matkul.append(matkul)
        
bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)

bowo.enrol("Basis Data")

print("Nama:", bowo.nama_depan, bowo.nama_belakang)
print("Nomor ID:", bowo.nomor_id)
print("jenjang:", bowo.jenjang)
print("Mata Kuliah yang diambil:", bowo.matkul[0])
