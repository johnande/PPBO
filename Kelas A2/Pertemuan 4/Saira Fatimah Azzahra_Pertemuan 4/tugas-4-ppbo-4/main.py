class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        
    def tampilkan_informasi(self):
        print("Nama Anda:", self.nama_depan, self.nama_belakang)
        print("Nomor ID Anda:", self.nomor_id)
        
class Karyawan(Orang):
    TETAP = "Tetap"
    TDK_TETAP = "Tidak Tetap"
    
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.status_karyawan = status_karyawan
        
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print("Status Karyawan:", self.status_karyawan)
        
class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        self.matkul_diajar = []
        
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
        
    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print("Mata kuliah yang Diajar adalah", self.matkul_diajar)
        
dosen1 = Dosen("James", "Smith", "321432", Karyawan.TETAP)
dosen1.mengajar("Database")
dosen1.tampilkan_informasi()
print()
dosen2 = Dosen("Janny", "Colyne", "543678", Karyawan.TDK_TETAP)
dosen2.mengajar("Matematika dan Elektronika")
dosen2.tampilkan_informasi()

        