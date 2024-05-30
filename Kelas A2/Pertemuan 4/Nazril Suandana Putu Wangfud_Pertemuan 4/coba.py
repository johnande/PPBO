#nomor 1
class Orang:
    def __init__(self, nama_depan, nama_belakang, no_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.no_id = no_id

    def tampilkan_info(self):
        print(f"Nama depan: ",self.nama_depan)
        print(f"nama belakang", self.nama_belakang)
        print(f"No. ID: ",self.no_id)

# orang1 = Orang("Nazril", "wangfud", 516054)
# orang1.tampilkan_info()

#nomor 2
class Mahasiswa(Orang):
    SARJANA = "SARJANA"
    MASTER = "MASTER"
    DOKTOR = "DOKTOR"

    def __init__(self, nama_depan, nama_belakang, no_id, jenjang):
        super().__init__(nama_depan, nama_belakang, no_id)
        self.jenjang = jenjang
        self.matkul = []
   
    def enrol(self, matkul):
        if matkul not in self.matkul:
            self.matkul.append(matkul)

    def cetak(self):
        print(f"Nama depan:" ,self.nama_depan)
        print(f"Nama belakang: ",self.nama_belakang)
        print(f"Nomer ID: ",self.no_id)
        print(f"Jenjang: ",self.jenjang)
        print(f"matkul : ",self.matkul)
    
# print()
# mahasiswa = Mahasiswa("Nazril", "wangfud", "516054", Mahasiswa.SARJANA)
# mahasiswa.enrol("Matematika")
# mahasiswa.enrol("Fisika")
# mahasiswa.cetak()

#nomor 3
class Karyawan(Orang):
    TETAP = "TETAP"
    TDK_TETAP = "TIDAK TETAP"

    def __init__(self, nama_depan, nama_belakang, no_id, status):
        super().__init__(nama_depan, nama_belakang, no_id)
        self.status = status

    def cetak(self):
        print()
        print(f"Nama depan:" ,self.nama_depan)
        print(f"Nama belakang: ",self.nama_belakang)
        print(f"Nomer ID: ",self.no_id)
        print(f"Status: ",self.status)

# print()
# karyawan = Karyawan("Asep", "Kurnia", "555555", Karyawan.TETAP)
# karyawan.cetak()

#nomor 4
class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, no_id, status):
        super().__init__(nama_depan, nama_belakang, no_id, status)
        self.matkul_diajar = []

    def mengajar(self, matkul):
        if matkul not in self.matkul_diajar:
            self.matkul_diajar.append(matkul)

    def cetak(self):
        print(f"Nama depan:" ,self.nama_depan)
        print(f"Nama belakang: ",self.nama_belakang)
        print(f"Nomer ID: ",self.no_id)
        print(f"matkul: ",self.matkul_diajar)
        print(f"status: ",self.status)
        
#nomor 5
print("====Mahasiswa====")
bowo = Mahasiswa("Bowo", "Nugroho", 987654, Mahasiswa.SARJANA)
bowo.enrol("Basis Data")
bowo.cetak()


#nomor 6
print("")
print("=====DOSEN=====")
rizki = Dosen(nama_depan="Rizki", nama_belakang="Setiabudi", 
              no_id="456789", status=Karyawan.TETAP)
rizki.mengajar("Statistik")
rizki.cetak()
print("")

#nomor 7
class Pelajar():
    def __init__(self):
        self.matkul = []

    def enrol(self, matkul):
        if matkul not in self.matkul:
            self.matkul.append(matkul)

#nomor 8
class Pengajar():
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, matkul):
        if matkul not in self.matkul_diajar:
            self.matkul_diajar.append(matkul)

# nomor 9
class Asdos(Orang, Pengajar, Pelajar):
    def __init__(self, nama_depan, nama_belakang, no_id):
        super().__init__(nama_depan, nama_belakang, no_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)
    
    def cetak(self):
        print(f"Nama depan:" ,self.nama_depan)
        print(f"Nama belakang: ",self.nama_belakang)
        print(f"Nomer ID: ",self.no_id)
        print(f"status: ",self.matkul)
        print(f"status: ",self.matkul_diajar)

#nomor 10
print("====ASDOS====")
uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisia")
uswatun.cetak()