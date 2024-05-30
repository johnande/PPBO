class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        
    def tampilkan_informasi(self):
        print("Nama Anda:", self.nama_depan, self.nama_belakang)
        print("Nomor ID Anda:", self.nomor_id)
        
class Mahasiswa(Orang):
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"
    
    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.jenjang = jenjang
        self.matkul = []
        
    def enrol(self, matkul):
        self.matkul.append(matkul)

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print("Jenjang", self.jenjang)
        print("Mata Kuliah yang diambil adalah", self.matkul)
    

mahasiswa = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
mahasiswa.enrol("Basis Data")
mahasiswa.tampilkan_informasi()
