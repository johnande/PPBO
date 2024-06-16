from abc import ABC, abstractclassmethod

class Universitas(ABC):
    def __init__(self, prodi):
        self.prodi = prodi

    @abstractclassmethod
    def info_univ(self):
        pass

    def info_prodi(self):
        pass

class UGM(Universitas):
    def __init__(self, prodi):
        super().__init__(prodi)

    def info_univ(self):
        print(f"Kampus: Universitas Gadjah Mada")

    def info_prodi(self):
        print(f"Program studi: {self.prodi}")

class UNY(Universitas):
    def __init__(self, prodi):
        super().__init__(prodi)

    def info_univ(self):
        print(f"Kampus: Universitas Negeri Yogyakarta")

    def info_prodi(self):
        print(f"Program studi: {self.prodi}")

# factory class
class Kampus:
    @staticmethod
    def mana_kampusmu(kampus, prodi):
        if kampus == "UGM":
            return UGM(prodi)
        elif kampus == "UNY":
            return UNY(prodi)
        else:
            print("Kampus tidak dikenali")

kampus = input("Nama kampus: ")
prodi = input("Nama program studi: ")
print()

mhs1 = Kampus.mana_kampusmu(kampus, prodi)
mhs1.info_univ()
mhs1.info_prodi()