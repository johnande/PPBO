class Orang :
    def __init__(self, nama_depan, nama_belakang, ID) -> None:
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.ID = ID

class Mahasiswa (Orang):

    SARJANA, MASTER, DOKTOR = range(3)

    def __init__(self, nama_depan, nama_belakang, ID, jenjang) -> None:
        super().__init__(nama_depan, nama_belakang, ID)
        self.jenjang = jenjang
        self.matkul = []

    def enrol (self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Karyawan (Orang):

    TETAP, TIDAK_TETAP = range(2)

    def __init__(self, nama_depan, nama_belakang, ID, status):
        super().__init__(nama_depan, nama_belakang, ID)
        self.status_karyawan = status

class Dosen (Karyawan):
    def __init__(self, nama_depan, nama_belakang, ID, status):
        super().__init__(nama_depan, nama_belakang, ID, status)
        self.dosen_matkul = []

    def mengajar (self, matkul):
        self.dosen_matkul.append(matkul)

bowo = Mahasiswa("Bowo", "Nugroho", 987654, Mahasiswa.SARJANA)
bowo.enrol("basis data")

rizki = Dosen("Rizki", "Setiabudi", 456789, Karyawan.TETAP)
rizki.mengajar("statistika")



class Pelajar:

    def __init__(self) -> None:
        self.belajar = []

    def enrol (self, mata_kuliah):
        self.belajar.append(mata_kuliah)

class Pengajar:

    def __init__(self) -> None:
        self.matkul_diajar = []

    def mengajar (self, matkul):
        self.matkul_diajar.append(matkul)

class Asdos (Orang, Pelajar, Pengajar):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.belajar = []
        self.matkul_diajar = []

uswatun = Asdos("Uswatun", "Hasanah", 456456)
uswatun.enrol("big data")
uswatun.mengajar("kecerdasan artifisial")

