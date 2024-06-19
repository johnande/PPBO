class Handphone:
    def __init__(self, merk, series):
        self.merk = merk
        self.series = series

    def info_handphone(self):
        print(f"Handphone {self.merk} series {self.series}")

handphone_pertama = Handphone("Iphone", "7+")
handphone_kedua = Handphone("Samsung", "S10")

handphone_pertama.info_handphone()
handphone_kedua.info_handphone()
