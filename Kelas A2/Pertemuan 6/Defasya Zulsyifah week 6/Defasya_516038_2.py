from abc import ABC, abstractmethod
import random

class Kendaraan(ABC):
    def __init__(self, nama, kecepatan):
        self.nama = nama
        self.kecepatan = kecepatan

    @abstractmethod
    def bergerak(self):
        pass

class Mobil(Kendaraan):
    def bergerak(self):
        print(f"{self.nama} sedang bergerak dengan kecepatan {self.kecepatan} km/jam")

class Sepeda(Kendaraan):
    def bergerak(self):
        print(f"{self.nama} sedang bergerak dengan kecepatan {self.kecepatan} km/jam")

class Perahu(Kendaraan):
    def bergerak(self):
        print(f"{self.nama} sedang berlayar dengan kecepatan {self.kecepatan} knot")

# Membuat objek-objek dari kelas turunan
mobil = Mobil("Toyota", 100)
sepeda = Sepeda("BMX", 20)
perahu = Perahu("Speedboat", 50)

# Memanggil metode bergerak() pada masing-masing objek
mobil.bergerak()
sepeda.bergerak()
perahu.bergerak()

