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

    def tampilkan(self):
        print("===Karyawan===")
        print("Nama: ", self.namdep, self.nambel)
        print("Nomor ID: ", self.nomor_id)
        print("Status: ", self.status)

karyawan1 = Karyawan("Novi", "Sushmita", 9, Karyawan.TETAP)
karyawan1.tampilkan()