class Orang:
    def __init__(self, namdep, nambel, nomor_id):
        self.namdep = namdep
        self.nambel = nambel
        self.nomor_id = nomor_id
    
    def tampilkan(self):
        print("===Orang===")
        print("Nama: ", self.namdep, self.nambel)
        print("Nomor ID: ", self.nomor_id)

orang1 = Orang("Novi", "Sushmita", 9)
orang1.tampilkan()