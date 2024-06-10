class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        
class Karyawan(Orang):
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"
    
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.status_karyawan = status_karyawan
        
class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        self.matkul_diajar = []
        
    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)
        
    def cetak_mata_kuliah_diajar(self):
        print("Mata kuliah yang diajar:")
        for matkul in self.matkul_diajar:
            print("- ", matkul)
            
dosen1 = Dosen("Marsa", "Carol", 34876, Karyawan.TETAP)
print("Nama:", dosen1.nama_depan, dosen1.nama_belakang)
print("Nomor ID:", dosen1.nomor_id)
print("Status Karyawan:", dosen1.status_karyawan)

dosen1.mengajar("SOJ")
dosen1.mengajar("TekTel")
dosen1.cetak_mata_kuliah_diajar()


