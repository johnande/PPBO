class Hewan:
    def bersuara(self):
        raise NotImplementedError

class Mamalia(Hewan):
    def melahirkan(self):
        raise NotImplementedError

class Anjing(Mamalia):
    def bersuara(self):
        print("Woof!")

    def melahirkan(self):
        print("Anjing melahirkan anak anjing.")

class Kucing(Mamalia):
    def bersuara(self):
        print("Meow!")

    def melahirkan(self):
        print("Kucing melahirkan anak kucing.")

class Burung(Hewan):
    def bersuara(self):
        print("Chirp!")

def tampilkan_suara(hewan):
    hewan.bersuara()

def tampilkan_melahirkan(hewan):
    if isinstance(hewan, Mamalia):
        hewan.melahirkan()
    else:
        print("Hewan ini tidak melahirkan.")

anjing = Anjing()
kucing = Kucing()
burung = Burung()

hewan_list = [anjing, kucing, burung]

for hewan in hewan_list:
    tampilkan_suara(hewan)

print()

for hewan in hewan_list:
    tampilkan_melahirkan(hewan)
