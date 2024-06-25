#No1

class Brokoli:
    def rasa(self):
        print("Pahit")

    def bentuk(self):
        print("Kembang kol")

class Wortel:
    def rasa(self):
        print("Manis")

    def bentuk(self):
        print("Silinder")

brokoli = Brokoli()
wortel = Wortel()

for sayur in (brokoli, wortel):
    sayur.rasa()
    sayur.bentuk()
