from collections import namedtuple

def add_informasi_mahasiswa(cls):
    def informasi_mahasiswa(self):
        print(f"Nama: {self.Nama}")
        print(f"NIM: {self.NIM}")
        print("Nilai:")
        for i, nilai in enumerate(self.Nilai, 1):
            if i == 1:
                matkul = "PBO"
            elif i == 2:
                matkul = "Basis Data"
            elif i == 3:
                matkul = "Jaringan Komputer"
            elif i == 4:
                matkul = "K3"
            else:
                matkul = "Matkul tidak terdaftar"
            print(f"{i}. {matkul}: {nilai}")
    cls.informasi_mahasiswa = informasi_mahasiswa
    return cls

Mahasiswa = namedtuple("Mahasiswa", ["Nama", "NIM", "Nilai"])
Mahasiswa = add_informasi_mahasiswa(Mahasiswa)
bintang = Mahasiswa(Nama="Bintang Berlian", NIM="518496", Nilai=[100, 90, 80, 85])
bintang.informasi_mahasiswa()