class Hewan:
    def jenis(self):
        print("Hewan ini adalah mamalia")
    def kaki(self):
        print("Ada yang berkaki empat, ada yang berkaki dua, ada juga yang tidak berkaki")

class Sapi(Hewan):
    def kaki(self):
        print("Sapi berkaki empat")

class Kanguru(Hewan):
    def kaki(self):
        print("Kanguru berkaki dua")

class Lumba(Hewan):
    def kaki(self):
        print("Lumba-lumba tidak memiliki kaki")

hewan = Hewan()
sapi = Sapi()
kanguru = Kanguru()
lumba = Lumba()

hewan.jenis()
hewan.kaki()
sapi.jenis()
sapi.kaki()
kanguru.jenis()
kanguru.kaki()
lumba.jenis()
lumba.kaki()
