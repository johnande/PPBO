class Orang:
    def __init__(self, namdep, nambel, nomor_id):
        self.namdep = namdep
        self.nambel = nambel
        self.nomor_id = nomor_id
    
class Mahasiswa(Orang):
    SARJANA, MASTER, DOKTOR = "Sarjana", "Master", "Doktor"
    def __init__(self, namdep, nambel, nomor_id, jenjang):
        super().__init__(namdep, nambel, nomor_id)
        self.jenjang = jenjang
        self.matkul = []

    def enroll(self, matkul):
        self.matkul.append(matkul)
    
    def tampilkan(self):
        print("===Mahasiswa===")
        print("Nama: ", self.namdep, self.nambel)
        print("Nomor ID: ", self.nomor_id)
        print("Jenjang: ", self.jenjang)
        print("Nama matkul diambil: ", self.matkul)

bowo = Mahasiswa("Bowo", "Nugroho", 987654, Mahasiswa.SARJANA)
bowo.enroll("Basis Data")
bowo.tampilkan()