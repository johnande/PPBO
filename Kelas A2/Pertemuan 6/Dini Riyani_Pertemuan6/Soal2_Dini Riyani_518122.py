from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, plat_nomor, jam_parkir):
        self.plat_nomor = plat_nomor
        self.jam_parkir = jam_parkir

    @abstractmethod
    def total_pembayaran(self):
        pass

class Mobil(Kendaraan):
    def total_pembayaran(self):
        return self.jam_parkir * 5000

class Motor(Kendaraan):
    def total_pembayaran(self):
        return self.jam_parkir * 3000

def proses_parkir(Kendaraan):
    print("Plat nomor kendaraan:", Kendaraan.plat_nomor)
    print("Jam Parkir:", Kendaraan.jam_parkir)
    print("Biaya Parkir:", Kendaraan.total_pembayaran())

if __name__ == "__main__":
    mobil = Mobil("ABC123", 2)
    motor = Motor("XYZ789", 3)

    print("Car:")
    proses_parkir(mobil)
    print("\nMotorcycle:")
    proses_parkir(motor)