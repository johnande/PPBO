class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        return f"Nama: {self.nama}"

    def bernapas(self):
        pass

class Burung(Hewan):
    def bernapas(self):
        return "Burung bernapas dengan aves."

class Belalang(Hewan):
    def bernapas(self):
        return "Belalang bernapas dengan trakea."

def pernapasan_hewan(hewan):
    print(hewan.info())
    print(hewan.bernapas())

burung =  Burung("Burung")
belalang = Belalang("Belalang")

pernapasan_hewan(burung)
pernapasan_hewan(belalang)