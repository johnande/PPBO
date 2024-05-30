from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, merek):
        self.merek = merek

    @abstractmethod
    def berkendara(self):
        pass

class Mobil(Kendaraan):
    def berkendara(self):
        print(f"Mobil",self.merek, "sedang berkendara di jalan toll.")

class Motor(Kendaraan):
    def berkendara(self):
        print(f"Motor",self.merek, "sedang melaju ke pasar.")

# Membuat objek dari kelas turunan
toyota_avanza = Mobil("Toyota Avanza")
honda_beat = Motor("Honda Beat")

# Memanggil metode berkendara
toyota_avanza.berkendara()
honda_beat.berkendara()