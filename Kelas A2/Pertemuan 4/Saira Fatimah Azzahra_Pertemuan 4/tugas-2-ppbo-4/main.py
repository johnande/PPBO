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
    
    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []
        
    def enrol(self, matkul):
        self.matkul.append(matkul)

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print("Jenjang", self.jenjang)
        print("Mata Kuliah yang diambil adalah", self.matkul)
    

mahasiswa1 = Mahasiswa("Saira", "Azzahra", "518201", Mahasiswa.SARJANA)
mahasiswa1.enrol("Praktikum Pemrograman Berbasis Objek")
mahasiswa1.enrol("Praktikum Teknik Telekomunikasi")
mahasiswa1.tampilkan_informasi()
print()
mahasiswa2 = Mahasiswa("Jane", "Priscila", "67890", Mahasiswa.DOKTOR)
mahasiswa2.enrol("Biologi")
mahasiswa2.enrol("Kimia")
mahasiswa2.tampilkan_informasi()
