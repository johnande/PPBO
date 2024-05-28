class Orang:
    def __init__(self, namdep, nambel, nomor_id):
        self.namdep = namdep
        self.nambel = nambel
        self.nomor_id = nomor_id
    
class Karyawan(Orang):
    TETAP, TDK_TETAP = "Tetap", "Tidak Tetap"
    def __init__(self, namdep, nambel, nomor_id, status):
        super().__init__(namdep, nambel, nomor_id)
        self.status = status

class Dosen(Karyawan):
    def __init__(self, namdep, nambel, nomor_id, status):
        super().__init__(namdep, nambel, nomor_id, status)
        self.matkul=[]
    
    def mengajar(self, matkul_diajar):
        self.matkul.append(matkul_diajar)

    def tampilkan(self):
        print("===Dosen===")
        print("Nama: ", self.namdep, self.nambel)
        print("Nomor ID: ", self.nomor_id)
        print("Status: ", self.status)
        print("Nama matkul diajar: ", self.matkul)

dosen1 = Dosen("Novi", "Sushmita", 9, Dosen.TETAP)
dosen1.mengajar("Pemrograman Komputer")
dosen1.tampilkan()