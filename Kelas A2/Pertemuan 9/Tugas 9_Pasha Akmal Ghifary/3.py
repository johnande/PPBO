# Definisikan kelas-kelas produk yang akan dibuat oleh factory
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    def berkendara(self):
        print(f"Mobil {self.merek} sedang berkendara.")

class Sepeda:
    def __init__(self, merek):
        self.merek = merek

    def mengayuh(self):
        print(f"Sepeda {self.merek} sedang mengayuh.")

# Definisikan kelas factory untuk membuat objek
class PabrikKendaraan:
    def create_vehicle(self, jenis_kendaraan, merek):
        if jenis_kendaraan == "mobil":
            return Mobil(merek)
        elif jenis_kendaraan == "sepeda":
            return Sepeda(merek)
        else:
            raise ValueError("Jenis kendaraan tidak valid")

# Penggunaan factory untuk membuat objek
pabrik = PabrikKendaraan()

mobil = pabrik.create_vehicle("mobil", "Toyota")
mobil.berkendara()

sepeda = pabrik.create_vehicle("sepeda", "Honda")
sepeda.mengayuh()
