class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

class Jenjang:
    SARJANA = "Sarjana"
    MASTER = "Master"
    DOKTOR = "Doktor"

class Mahasiswa(Orang):
    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class StatusKaryawan:
    TETAP = "Tetap"
    TDK_TETAP = "Tidak Tetap"

class Karyawan(Orang):
    def __init__(self, status_karyawan, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_karyawan = status_karyawan

class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

bowo = Mahasiswa( Jenjang.SARJANA, "Bowo", "Nugroho", "987654")
bowo.enrol("Basis Data")

rizki = Dosen(StatusKaryawan.TETAP, "Rizki", "Setiabudi", "456789")
rizki.mengajar("Statistik")