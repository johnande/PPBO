from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, merek, model, tahun, harga):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.harga = harga

    @abstractmethod
    def hitung_pajak(self):
        pass

    @abstractmethod
    def tampilkan_info(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, merek, model, tahun, harga, jumlah_pintu):
        super().__init__(merek, model, tahun, harga)
        self.jumlah_pintu = jumlah_pintu

    def hitung_pajak(self):
        return self.harga * 0.15

    def tampilkan_info(self):
        print(f"Mobil: {self.tahun} {self.merek} {self.model}, {self.jumlah_pintu} pintu, Harga: Rp{self.harga}")

class SepedaMotor(Kendaraan):
    def __init__(self, merek, model, tahun, harga, ukuran_mesin):
        super().__init__(merek, model, tahun, harga)
        self.ukuran_mesin = ukuran_mesin

    def hitung_pajak(self):
        return self.harga * 0.1

    def tampilkan_info(self):
        print(f"Sepeda Motor: {self.tahun} {self.merek} {self.model}, Ukuran Mesin: {self.ukuran_mesin}, Harga: Rp{self.harga}")

def main():
    mobil = Mobil("Toyota", "Camry", 2022, 25000, 4)
    sepeda_motor = SepedaMotor("Honda", "CBR500R", 2023, 8000, "500cc")
    
    kendaraan = [mobil, sepeda_motor]

    for kend in kendaraan:
        kend.tampilkan_info()
        print(f"Pajak: Rp{kend.hitung_pajak()}")

if __name__ == "__main__":
    main()

