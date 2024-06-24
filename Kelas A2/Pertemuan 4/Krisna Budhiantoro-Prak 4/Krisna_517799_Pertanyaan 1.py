class BangunDatar:
    def hitungLuas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi * self.sisi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitungLuas(self):
        return 3.14 * self.jari_jari * self.jari_jari

def main():
    persegi = Persegi(5)
    lingkaran = Lingkaran(7)

    print("Luas Persegi:", persegi.hitungLuas())
    print("Luas Lingkaran:", lingkaran.hitungLuas())

if __name__ == "__main__":
    main()
