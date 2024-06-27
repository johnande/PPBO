class Handphone:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info_handphone(self):
        print("Handphone merk", self.merk, "tahun", self.tahun)

handphone1 = Handphone("Samsung", 2022)
handphone2 = Handphone("Oppo", 2020)
handphone1.info_handphone()
handphone2.info_handphone()
