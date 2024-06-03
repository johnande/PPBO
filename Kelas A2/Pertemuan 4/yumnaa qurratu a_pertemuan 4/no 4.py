class Karyawan:
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        self.status_karyawan = status_karyawan

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        self.matkul_diajar = []  
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

dosen1 = Dosen("Budi", "Doremi", 12345, Karyawan.TETAP)
print("Nama Dosen:", dosen1.nama_depan, dosen1.nama_belakang)
print("Nomor ID Dosen:", dosen1.nomor_id)
print("Status Karyawan:", dosen1.status_karyawan)

dosen1.mengajar("Pemrograman Komputer")
dosen1.mengajar("Basis Data")

print("Mata Kuliah yang Diajar:", dosen1.matkul_diajar)

