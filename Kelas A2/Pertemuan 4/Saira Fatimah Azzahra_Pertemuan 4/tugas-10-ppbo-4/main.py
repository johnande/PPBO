class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id
        
    def tampilkan_informasi(self):
        print("Nama Anda:", self.nama_depan, self.nama_belakang)
        print("Nomor ID Anda:", self.nomor_id)

class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, matkul):
        self.matkul.append(matkul)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, matkul):
        self.matkul_diajar.append(matkul)
        
class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_id):
        super().__init__(nama_depan, nama_belakang, nomor_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

    def tampilkan_informasi(self):
        super().tampilkan_informasi()
        print("Mata kuliah yang diambil:", self.matkul)
        print("Mata kuliah yang diajar:", self.matkul_diajar)

nama = Asdos("Uswatun", "Hasanah", "456456")
nama.enrol("Big Data")
nama.mengajar("Kecerdasan Artifisial")
nama.tampilkan_informasi()
