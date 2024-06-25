#Soal 1-6 (1)

class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

    def get_full_name(self):
        return f"{self.nama_depan} {self.nama_belakang}"

    def id_number(self):
        return self.nomor_id

class Mahasiswa(Orang):
    def __init__(self, nama_depan, nama_belakang, nomor_id, jenjang, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, *args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    SARJANA, MASTER, DOKTOR = range(3)

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

    def level(self):
        if self.jenjang == self.SARJANA:
            return "Sarjana"
        elif self.jenjang == self.MASTER:
            return "Master"
        elif self.jenjang == self.DOKTOR:
            return "Doktor"

class Karyawan(Orang):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, *args, **kwargs)
        self.status_karyawan = status_karyawan

    TETAP, TIDAK_TETAP = range(2)

    def status(self):
        return "Karyawan Tetap" if self.status_karyawan == self.TETAP else "Karyawan Tidak Tetap"

class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_id, status_karyawan, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, status_karyawan, *args, **kwargs)
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

    def level(self):
        return "Dosen"

bowo = Mahasiswa("Bowo", "Nugroho", 987654, Mahasiswa.SARJANA)
bowo.enrol("Basis Data")

print(f"Nama lengkap: {bowo.get_full_name()}")
print(f"Nomer ID: {bowo.id_number()}")
print(f"Jenjang: {bowo.level()}")
print(f"Mata kuliah yang diambil: {bowo.matkul}")

rizki = Dosen("Rizki", "Setiabudi", 456789, Dosen.TETAP)
rizki.mengajar("Statistik")

print(f"Nama lengkap: {rizki.get_full_name()}")
print(f"Nomer ID: {rizki.id_number()}")
print(f"Status Karyawan: {rizki.status()}")
print(f"Mata kuliah yang diajar: {rizki.matkul_diajar}")
