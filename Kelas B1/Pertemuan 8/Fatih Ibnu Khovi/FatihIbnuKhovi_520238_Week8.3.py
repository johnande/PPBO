from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, model, harga):
        self.model = model
        self.harga = harga
    
    @abstractmethod
    def tampilan_kendaraan(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, model, harga, warna):
        super().__init__(model, harga)
        self.warna = warna
    
    def tampilan_kendaraan(self):
        return f"Model Mobil: {self.model}, Warna: {self.warna}, Harga: Rp {self.harga}"

class Motor(Kendaraan):
    def __init__(self, model, harga, merek):
        super().__init__(model, harga)
        self.merek = merek
    
    def tampilan_kendaraan(self):
        return f"Model Motor: {self.model}, Merek: {self.merek}, Harga: Rp {self.harga}"

mobil = Mobil("Ferrari sf90", 7000000000, "Red")
print("Informasi Mobil:")
print(mobil.tampilan_kendaraan())

motor = Motor("Supra Bapak", 19000000, "Honda")
print("\nInformasi Motor:")
print(motor.tampilan_kendaraan())