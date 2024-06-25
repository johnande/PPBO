class Alat_musik:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model

    def dimainkan(self):
        print("Dimainkan")

class Gitar(Alat_musik):
    pass

class Suling(Alat_musik):
    def dimainkan(self):
        print("Ditiup")

class Gendang(Alat_musik):
    def dimainkan(self):
        print("Dipukul")

gitar1 = Gitar("Yamaha", "Elektrik")
suling1 = Suling("Yamaha", "Klasik")
gendang1 = Gendang("Jogja", "Kraton")

for x in (gitar1, suling1, gendang1):
    print(x.merk)
    print(x.model)
    x.dimainkan()