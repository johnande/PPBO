class Jateng:
    def rumah_adat(self):
        print("Rumah adat Jawa Tengah: Joglo")

    def makanan_khas(self):
        print("Makanan khas Jawa Tengah: Gudeg, Soto")

class Jabar:
    def rumah_adat(self):
        print("Rumah adat Jawa Barat: Rumah Panggung")

    def makanan_khas(self):
        print("Makanan khas Jawa Barat: Sate, Batagor")

class Jatim:
    def rumah_adat(self):
        print("Rumah adat Jawa Timur: Rumah Gadang")

    def makanan_khas(self):
        print("Makanan khas Jawa Timur: Rawon, Sate Madura")


jateng = Jateng()
jabar = Jabar()
jatim = Jatim()

for keberagaman in (jateng, jabar, jatim):
    keberagaman.rumah_adat()
    keberagaman.makanan_khas()
    print()
