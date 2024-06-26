#================================================================ Soal nomor 1
class orang:
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_ID = nomor_ID
        self.matkul = []
        self.matkul_diajar = []
        
#================================================================ Soal nomor 2
class mahasiswa(orang):
    SARJANA, MASTER, DOKTOR = range(3)
    def __init__(self, nama_depan, nama_belakang, nomor_ID, jenjang):
        super().__init__(nama_depan, nama_belakang, nomor_ID)
        self.jenjang = jenjang
        self.matkul = []
        if jenjang == 0:
            self.jenjang = "Sarjana"
        elif jenjang == 1:
            self.jenjang = "Master"
        elif jenjang == 2:
            self.jenjang = "Doktor"
    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

#================================================ Soal nomor 3
class karyawan(orang):
    TETAP, TDK_TETAP = range(2)
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
      super().__init__(nama_depan, nama_belakang, nomor_ID)
      self.status_karyawan = status_karyawan
      if status_karyawan == 0:
          self.status_karyawan = "TETAP"
      elif status_karyawan == 1:
          self.status_karyawan = "TDK TETAP"
      else:
          self.status_karyawan = "BUKAN KARYAWAN"

#================================================================ Soal nomor 4
class dosen(karyawan):
    def __init__(self, nama_depan, nama_belakang, nomor_ID, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomor_ID, status_karyawan)
        self.matkul_diajar = []
    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)
        
#================================================================ Soal nomor 5
bowo = mahasiswa("Bowo", "Nugroho", "987654", mahasiswa.SARJANA)
bowo.enrol("Basis Data")

print("\nNama: ", bowo.nama_depan, bowo.nama_belakang)
print("Nomor ID: ", bowo.nomor_ID)
print("Jenjang: ", bowo.jenjang)
print("Mata kuliah: ", bowo.matkul)

#=============================================================== Soal nomor 6
rizki = dosen("Rizki", "Setiabudi", "456789", karyawan.TETAP)
rizki.mengajar("Statisik")

print("\nNama: ", rizki.nama_depan, rizki.nama_belakang)
print("Nomor ID: ", rizki.nomor_ID)
print("Status Karyawan: ", rizki.status_karyawan)
print("Mata kuliah: ", rizki.matkul_diajar)

#============================================================== Soal nomor 7
class pelajar:
    def __init__(self):
        self.matkul = []
    def enrol (self, mata_kuliah):
        self.matkul.append(mata_kuliah)

#============================================================== Soal nomor 8
class pengajar:
    def __init__(self):
        self.matkul_diajar = []
    def mengajar(self, matkul_diajar):
        self.matkul_diajar.append(matkul_diajar)

#============================================================== Soal nomor 9
class asdos(orang, pelajar, pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_ID):
        super().__init__(nama_depan, nama_belakang, nomor_ID)

#============================================================= Soal nomor 10     
uswatun = asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

print("\nNama: ", uswatun.nama_depan, uswatun.nama_belakang)
print("Nomor ID: ", uswatun.nomor_ID)
print("Mata kuliah: ", uswatun.matkul)
print("Mengajar: ", uswatun.matkul_diajar)