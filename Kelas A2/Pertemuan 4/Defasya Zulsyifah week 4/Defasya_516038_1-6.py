# Nomor 1: Membuat kelas Orang dengan atribut nama_depan, nama_belakang, dan nomor_ID
class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID

# Nomor 2: Membuat kelas Mahasiswa yang merupakan turunan dari kelas Orang
class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"

    def __init__(self, nama_depan, nama_belakang, nomor_ID, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

# Nomor 3: Membuat kelas Karyawan yang merupakan turunan dari kelas Orang
class Karyawan(Orang):
    TETAP = "TETAP"
    TIDAK_TETAP = "TDK_TETAP"

    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.status_karyawan = status_karyawan

# Nomor 4: Membuat kelas Dosen yang merupakan turunan dari kelas Karyawan
class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

# Nomor 5: Membuat objek bowo menggunakan kelas Mahasiswa
bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
bowo.enrol("Basis Data")

# Nomor 6: Membuat objek rizki menggunakan kelas Dosen
rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
rizki.mengajar("Statistik")
