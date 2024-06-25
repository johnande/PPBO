#nomor 1
class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

#nomor 2
class Mahasiswa(Orang):
    def __init__(self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class jenjang :
    SARJANA = "SARJANA"
    MAGISTER = "MAGISTER"
    DOKTOR = "DOKTOR"

#nomor 3
class Karyawan(Orang):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs,)
        self.status_karyawan = status_karyawan

class status_karyawan:
    TETAP = "TETAP"
    TDK_TETAP = "TDK_TETAP"

#nomor 4
class Dosen(Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_ajar = []
    def mengajar(self, matkul_ajar):
        self.matkul_ajar.append(matkul_ajar)

#nomor 5
bowo = Mahasiswa("Bowo", "Nugroho", "987654", jenjang.SARJANA)
bowo.enrol("Basis Data")

#nomor 6
rizki = Dosen("Rizki", "Setiabudi", "456789", status_karyawan.TETAP)
rizki.mengajar("Statistik")