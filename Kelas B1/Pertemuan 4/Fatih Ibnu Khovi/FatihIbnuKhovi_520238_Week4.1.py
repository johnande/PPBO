class orang:
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID
        self.matkul = []
        self.mengampu_matkul = []


class mahasiswa(orang):
    SARJANA, MASTER, DOKTOR = range(3)

    def __init__(self, nama_depan, nama_belakang, nomor_ID, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.jenjang = jenjang
        if jenjang == 0:
            self.jenjang = "Sarjana"
        elif jenjang == 1:
            self.jenjang = "Master"
        elif jenjang == 2:
            self.jenjang = "Doktor"
        else:
            self.jenjang = "Jenjang Tidak Terdaftar"

        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)


class karyawan(orang):
    TETAP, TDK_TETAP = range(2)

    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.status_karyawan = status_karyawan
        if status_karyawan == 0:
            self.status_karyawan = "Tetap"
        elif status_karyawan == 1:
            self.status_karyawan = "Tidak Tetap"
        else:
            self.status_karyawan = "Status Karyawan Tidak Terdaftar"


class dosen(karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID, status_karyawan)
        self.mengampu_matkul = []

    def mengajar(self, matkul_diajar):
        self.mengampu_matkul.append(matkul_diajar)


bowo = mahasiswa("Bowo", "Nugroho", "987654", 0)
bowo.enrol("Basis Data")
print("Nama:", bowo.nama_depan, bowo.nama_belakang,
      "\nID Mahasiswa:", bowo.nomor_ID,
      "\nJenjang:", bowo.jenjang,
      "\nMata Kuliah Yang Diambil:", bowo.matkul)

print(" ")

rizki = dosen("Rizki", "Setiabudi", "456789", 0)
rizki.mengajar("Statistik")
print("Nama:", rizki.nama_depan, rizki.nama_belakang,
      "\nID Dosen:", rizki.nomor_ID,
      "\nStatus Karyawan:", rizki.status_karyawan,
      "\nMengajar Mata Kuliah", rizki.mengampu_matkul)


class pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)


class pengajar:
    def __init__(self):
        self.mengampu_matkul = []

    def mengajar(self, matkul_diajar):
        self.mengampu_matkul.append(matkul_diajar)


class asdos(orang, pelajar, pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        super().__init__(nama_depan, nama_belakang, nomor_ID)


uswatun = asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")


print("\nNama:", uswatun.nama_depan, uswatun.nama_belakang,
      "\nID Asdos:", uswatun.nomor_ID,
      "\nMata kuliah yang diambil:", uswatun.matkul,
      "\nMata kuliah yang diajar:", uswatun.mengampu_matkul)