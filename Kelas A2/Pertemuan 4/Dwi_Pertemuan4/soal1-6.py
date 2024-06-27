class Orang:
    def __init__ (self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

class Mahasiswa(Orang):
    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.jenjang = jenjang
        self.matkul = []
    def enrol(self, matkul):
        self.matkul.append(matkul)

class jenjang:
    SARJANA = "SARJANA"
    MAGISTER = "MAGISTER"
    DOKTOR = "DOKTOR"

class Karyawan(Orang):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        self.status_karyawan = status_karyawan

class status_karyawan:
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan)
        self.matkul_ajar = []
    def mengajar(self, matkul_ajar):
        self.matkul_ajar.append(matkul_ajar)

#Pemanggilan objek
bowo = Mahasiswa("Bowo", "Nugroho", "987654", jenjang.SARJANA)
bowo.enrol("Basis Data")

rizki = Dosen("Rizki", "Setiabudi", "456789", status_karyawan.TETAP)
rizki.mengajar("Statistik")
