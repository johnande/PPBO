from abc import ABC, abstractmethod

# Abstract base class (ABC)
class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass
    
    @abstractmethod
    def keliling(self):
        pass

# Inheritance: Circle subclass dari BangunDatar
class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    # Implementasi method luas
    def luas(self):
        return 3.14 * self.jari_jari**2
    
    # Implementasi method keliling
    def keliling(self):
        return 2 * 3.14 * self.jari_jari

# Inheritance: Rectangle subclass dari BangunDatar
class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    # Implementasi method luas
    def luas(self):
        return self.panjang * self.lebar
    
    # Implementasi method keliling
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

# Polymorphism: fungsi untuk menghitung luas total dari beberapa bangun datar
def hitung_luas_total(bangun_datar_list):
    total = 0
    for bangun_datar in bangun_datar_list:
        total += bangun_datar.luas()
    return total

# Polymorphism: fungsi untuk menghitung keliling total dari beberapa bangun datar
def hitung_keliling_total(bangun_datar_list):
    total = 0
    for bangun_datar in bangun_datar_list:
        total += bangun_datar.keliling()
    return total

# Membuat objek-objek
lingkaran = Lingkaran(5)
persegi_panjang = PersegiPanjang(4, 6)

# Polymorphism: memasukkan objek-objek ke dalam list
bangun_datar_list = [lingkaran, persegi_panjang]

# Menggunakan fungsi-fungsi untuk menghitung luas dan keliling total
luas_total = hitung_luas_total(bangun_datar_list)
keliling_total = hitung_keliling_total(bangun_datar_list)

print("Luas total: ", luas_total)
print("Keliling total: ", keliling_total)
