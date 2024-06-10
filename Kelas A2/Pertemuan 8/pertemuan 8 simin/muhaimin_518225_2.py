from abc import ABC, abstractmethod

class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def hitung_luas(self):
        return 3.14 * self.jari_jari ** 2

def main():
    persegi = Persegi(5)
    lingkaran = Lingkaran(7)

    print("Luas persegi:", persegi.hitung_luas())
    print("Luas lingkaran:", lingkaran.hitung_luas())

if __name__ == "__main__":
    main()
