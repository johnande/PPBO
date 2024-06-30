class Buah:
    def Jenis(self):
        print("Ada banyak sekali jenis buah-buahan")
    def Nama(self):
        print("Ada banyak macam nama buah")
    def Warna(self):
        print("Ada banyak macam warna buah")
    def Rasa(self):
        print("Ada banyak macam rasa buah\n")

class Apel(Buah):
    def Nama(self):
        print("Buah ini namanya apel")
    def Warna(self):
        print("Buah ini warnanya merah")
    def Rasa(Self):
        print("Buah ini rasanya manis\n")

class Belimbing(Buah):
    def Nama(self):
        print("Buah ini namanya belimbing")
    def Warna(self):
        print("Buah ini warnanya kuning")
    def Rasa(self):
        print("Buah ini rasanya asam\n")
        
buah = Buah()
apel = Apel()
belimbing = Belimbing()

for buah in (buah, apel, belimbing):
    buah.Jenis()
    buah.Nama()
    buah.Warna()
    buah.Rasa()

    