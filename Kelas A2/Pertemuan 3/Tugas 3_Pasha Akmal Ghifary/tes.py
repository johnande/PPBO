class Hewan:
    def __init__(self, name):
        self.name = name

    def bunyi(self):
        pass

class Anjing(Hewan):
    def bunyi(self):
        print(f"{self.name} bersuara guk guk!!")

class Kucing(Hewan):
    def bunyi(self):
        print(f"{self.name} bersuara meongg!!")


anjing = Anjing("maul")
kucing = Kucing("milo")


anjing.bunyi()
kucing.bunyi()
