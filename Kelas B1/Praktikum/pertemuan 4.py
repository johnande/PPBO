#================================================================ Soal 1
class Herbivora:
    def makanan(self):
        print("\nHewan pemakan tumbuhan")
    def bentuk_gigi(self):
        print("Bentuk gigi dominan geraham")
    def bentuk_mata(self):
        print("Pupil mata berbentuk horizontal")

class Karnivora:
    def makanan(self):
        print("\nHewan pemakan daging")
    def bentuk_gigi(self):
        print("Bentuk gigi dominan taring")
    def bentuk_mata(self):
        print("Pupil mata berbentuk vertikal")

class Omnivora:
    def makanan(self):
        print("\nHewan pemakan daging dan tumbuhan")
    def bentuk_gigi(self):
        print("Bentuk gigi gabungan antara taring dan geraham")
    def bentuk_mata(self):
        print("Pupil mata berbentuk bulat")

kambing = Herbivora()
kucing = Karnivora()
simpanse = Omnivora()

for hewan in (kambing, kucing, simpanse):
    hewan.makanan()
    hewan.bentuk_gigi()
    hewan.bentuk_mata()
#================================================================ Soal 2
class Karnivora:
    def intro(self):
        print("Banyak hewan berjenis karnivora.")
    def makanan(self):
        print("Hewan berjenis karnivora adalah pemakan daging")

class Harimau(Karnivora):
    def makanan(self):
        print("Harimau adalah pemakan daging")

class Rusa(Karnivora):
    def makanan(self):
        print("Rusa adalah pemakan tumbuhan")


harimau = Harimau()
rusa = Rusa()

harimau.intro()
harimau.makanan()

rusa.intro()
rusa.makanan()
#================================================================ Soal 3
class Barang:
    def __init__(self, merek, harga_satuan):
        self.merek = merek
        self.harga_satuan = harga_satuan  # dalam ribu

    def mul(self, kuantitas):
        print('Banyaknya penjualan:', kuantitas.qty_jual, 'buah')
        return self.harga_satuan * kuantitas.qty_jual

class Penjualan:
    def __init__(self, merek, qty_jual):
        self.merek = merek
        self.qty_jual = qty_jual

redmi10 = Barang("Redmi10", 2140)
qty_maret = Penjualan("Redmi10", 20)
print(f"Total penjualan {redmi10.merek}: {redmi10.mul(qty_maret)} ribu")

#================================================================ Soal 4
class Binatang:
    def __init__(self, nama):
        self.nama = nama

    def __str__(self):
        return f"Binatang: {self.nama}"

    def __add__(self, other):
        return f"{self.nama} dan {other.nama} adalah teman binatang."

    def __sub__(self, other):
        return f"{self.nama} dan {other.nama} sedang bertengkar."

class Mamalia(Binatang):
    def __init__(self, nama, jenis):
        super().__init__(nama)
        self.jenis = jenis

    def __str__(self):
        return f"Mamalia ({self.jenis}): {self.nama}"

    def __mul__(self, n):
        return f"{self.nama} berjumlah {n} ekor."

kucing = Mamalia("Kucing", "Felidae")
anjing = Mamalia("Anjing", "Canidae")

print(anjing)
print(kucing)
print(kucing + anjing)  
print(kucing - anjing)  
print(anjing * 3)       

