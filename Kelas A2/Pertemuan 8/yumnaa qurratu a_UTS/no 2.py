from abc import ABC, abstractmethod

# Abstract Base Class (ABC)
class BangunDatar(ABC):

    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

# Subclass dari BangunDatar
class Persegi(BangunDatar):

    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

# Subclass dari BangunDatar
class Lingkaran(BangunDatar):

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari ** 2

    def keliling(self):
        return 2 * 3.14 * self.jari_jari

# Polymorphism dengan fungsi
def info_bangun_datar(bangun_datar):
    print(f"Luas: {bangun_datar.luas()}")
    print(f"Keliling: {bangun_datar.keliling()}")

# Membuat objek
persegi = Persegi(5)
lingkaran = Lingkaran(7)

# Memanggil fungsi dengan objek dari berbagai class
print("Info Persegi:")
info_bangun_datar(persegi)  
# Output:
# Luas: 25
# Keliling: 20

print("\nInfo Lingkaran:")
info_bangun_datar(lingkaran)  
# Output:
# Luas: 153.86
# Keliling: 43.96

