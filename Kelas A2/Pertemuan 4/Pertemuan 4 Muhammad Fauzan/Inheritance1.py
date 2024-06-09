class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

class Mahasiswa(Orang):
    Sarjana = "Sarjana"
    Master = "Master"
    Doktor = "Doktor"

    def __init__ (self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul =[]

    def enrol(self, MatKul):
        self.matkul.append(MatKul)

    def cetak(self):
        print(f"Nama = {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID = {self.nomor_id}")
        print(f"Jenjang = {self.jenjang}")
        print(f"Mata Kuliah = {self.matkul}")
        print(" ")

class karyawan(Orang):
    Tetap = "TETAP"
    Tidak_tetap = "TDK TETAP"

    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = status

    def cetak(self):
        print(f"Nama = {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID = {self.nomor_id}")
        print(f"Status Karyawan = {self.status}")
        print(" ")

class Dosen(karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)

    def cetak(self):
        print(f"Nama = {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID = {self.nomor_id}")
        print(f"Status Karyawan = {self.status}")
        print(f"Mata Kuliah = {self.matkul_diajar}")
        print(" ")

bowo = Mahasiswa(Mahasiswa.Sarjana, "Bowo", "Nugroho", 987654)
bowo.enrol("Basis Data")
bowo.cetak()

rizki = Dosen(Dosen.Tetap, "Rizki", "Setiabudi", 456789)
rizki.mengajar("Statistik")
rizki.cetak()

class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol (self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar (self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

    def cetak(self):
        print(f"Nama = {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID = {self.nomor_id}")
        print(f"Mata Kuliah = {self.matkul}")
        print(f"Mata Kuliah Diajar = {self.matkul_diajar}")
        print(" ")
        
uswatun = Asdos("Uswatun", "Hasanah", 456456)
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")
uswatun.cetak()
