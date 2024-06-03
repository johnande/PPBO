class Kendaraan:
    def __init__(self, nama, kecepatan_max):
        self.nama = nama
        self.kecepatan_max = kecepatan_max

    def info(self):
        return f"Kendaraan {self.nama} dengan kecepatan maksimum {self.kecepatan_max} km/jam."

class Mobil(Kendaraan):
    def __init__(self, nama, kecepatan_max, jumlah_penumpang):
        super().__init__(nama, kecepatan_max)
        self.jumlah_penumpang = jumlah_penumpang

    def info(self):
        return super().info() + f" Memiliki kapasitas penumpang sebanyak {self.jumlah_penumpang} orang."

class SepedaMotor(Kendaraan):
    def __init__(self, nama, kecepatan_max, tipe_mesin):
        super().__init__(nama, kecepatan_max)
        self.tipe_mesin = tipe_mesin

    def info(self):
        return super().info() + f" Dengan tipe mesin {self.tipe_mesin}."

def main():
    sedan = Mobil("Sedan", 180, 5)
    motor = SepedaMotor("Honda", 150, "4 Tak")

    print(sedan.info())
    print(motor.info())

if __name__ == "__main__":
    main()
