class Liburan:
    def kendaraan(self):
        pass

class Motor(Liburan):
    def kendaraan(self):
        return "Liburan menggunakan kendaraan motor lebih cepat"
    
class Mobil(Liburan):
    def kendaraan(self):
        return "Liburan menggunakan kendaraan mobil lebih nyaman"
    
class Factory:
    @staticmethod
    def buat_produk(jenis_produk):
        if jenis_produk == "Motor":
            return Motor()
        elif jenis_produk == "Mobil":
            return Mobil()
        else:
            raise ValueError("Tidak liburan menggunakan kendaraan lain")

# Penggunaan Factory Pattern
liburan1 = Factory.buat_produk("Motor")
print(liburan1.kendaraan())
liburan2 = Factory.buat_produk("Mobil")
print(liburan2.kendaraan())