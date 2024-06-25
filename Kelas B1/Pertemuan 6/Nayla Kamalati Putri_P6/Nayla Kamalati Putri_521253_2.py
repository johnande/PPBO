#No2

from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    @abstractmethod
    def total_harga(self):
        pass

class Laptop(BarangElektronik):
    def total_harga(self):
        return self.harga * self.jumlah

class Smartphone(BarangElektronik):
    def total_harga(self):
        return self.harga * self.jumlah

def proses_penjualan(barang):
    print("Nama Barang:", barang.nama)
    print("Harga per Barang:", barang.harga)
    print("Jumlah Barang:", barang.jumlah)
    print("Total Harga:", barang.total_harga())

if __name__ == "__main__":
    laptop = Laptop("Laptop Asus", 10000000, 3)
    smartphone = Smartphone("Smartphone Samsung", 5000000, 5)

    print("Penjualan Laptop:")
    proses_penjualan(laptop)

    print("\nPenjualan Smartphone:")
    proses_penjualan(smartphone)
