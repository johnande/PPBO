class Headphones:
    def __init__(self, merk, series):
        self.merk = merk
        self.series = series

    def info_Handphone(self):
        print(f"Handphone ({self.merk}) series ({self.series})")

# Membuat objek menggunakan konstruktor
Handphone_saya = Headphones("Iphone", "7+")

print(Handphone_saya.merk)
print(Handphone_saya.series)

Handphone_saya.info_Handphone()
