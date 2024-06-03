class Hewan:
    def bersuara(self):
        raise NotImplementedError

class Anjing(Hewan):
    def bersuara(self):
        print("Woof!")

class Kucing(Hewan):
    def bersuara(self):
        print("Meow!")

class Burung(Hewan):
    def bersuara(self):
        print("Chirp!")

def tampilkan_suara(hewan):
    hewan.bersuara()

anjing = Anjing()
kucing = Kucing()
burung = Burung()

hewan_list = [anjing, kucing, burung]

for hewan in hewan_list:
    tampilkan_suara(hewan)
