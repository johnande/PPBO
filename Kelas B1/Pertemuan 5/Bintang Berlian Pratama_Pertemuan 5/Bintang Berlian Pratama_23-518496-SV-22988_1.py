class Apel:
    def Nama(self):
        print("Ini Apel")
    def Warna(self):
        print("Buah ini warnanya merah")
    def Rasa(Self):
        print("Buah ini rasanya manis\n")

class Belimbing:
    def Nama(self):
        print("Ini Belimbing")
    def Warna(self):
        print("Buah ini warnanya kuning")
    def Rasa(self):
        print("Buah ini rasanya asam\n")
        
apel = Apel()
belimbing = Belimbing()

for buah in (apel, belimbing):
    buah.Nama()
    buah.Warna()
    buah.Rasa()