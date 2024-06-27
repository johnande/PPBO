class Binatang:
    def suara(self):
        pass

class Kucing(Binatang):
    def suara(self):
        return "Meow!"

class Anjing(Binatang):
    def suara(self):
        return "Woof!"

class Bebek(Binatang):
    def suara(self):
        return "Kwek kwek!"


binatang_koleksi = [Kucing(), Anjing(), Bebek()]

for binatang in binatang_koleksi:
        print(f"{type(binatang).__name__}: {binatang.suara()}")

