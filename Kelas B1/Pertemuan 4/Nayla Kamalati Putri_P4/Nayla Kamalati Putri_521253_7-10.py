#Soal 7-10

class Orang:
    def __init__(self, nama_depan, nama_belakang, nomor_id, *args, **kwargs):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomor_id = nomor_id

class Pelajar:
    def __init__(self, *args, **kwargs):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self, *args, **kwargs):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomor_id, *args, **kwargs):
        super().__init__(nama_depan, nama_belakang, nomor_id, *args, **kwargs)
        self.matkul = []
        self.matkul_diajar = []

    def info(self):
        info_str = f"Nama lengkap: {self.nama_depan} {self.nama_belakang}\nNomor ID: {self.nomor_id}\n"
        info_str += "Mata kuliah yang diambil: " + ", ".join(self.matkul) + "\n"
        info_str += "Mata kuliah yang diajar: " + ", ".join(self.matkul_diajar)
        return info_str

uswatun = Asdos("Uswatun", "Hasanah", 456456)

uswatun.enrol("Big Data")

uswatun.mengajar("Kecerdasan Artifisial")

print(uswatun.info())
