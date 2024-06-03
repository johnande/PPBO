from abc import ABC, abstractmethod

class Produk(ABC):
  """Kelas abstrak untuk produk yang dijual di toko online."""

  def __init__(self, nama, harga):
    self.nama = nama
    self.harga = harga

  @abstractmethod
  def hitung_diskon(self, diskon):
    pass

class Elektronik(Produk):
  """Kelas untuk produk elektronik yang dijual di toko online."""

  def __init__(self, nama, harga, garansi):
    super().__init__(nama, harga)
    self.garansi = garansi

  def hitung_diskon(self, diskon):
    diskon_elektronik = diskon * 0.8
    harga_diskon = self.harga - diskon_elektronik
    return harga_diskon

class Fashion(Produk):
  """Kelas untuk produk fashion yang dijual di toko online."""

  def __init__(self, nama, harga, ukuran):
    super().__init__(nama, harga)
    self.ukuran = ukuran

  def hitung_diskon(self, diskon):
    diskon_fashion = diskon * 0.7
    harga_diskon = self.harga - diskon_fashion
    return harga_diskon

def hitung_total(produk, diskon):
  """Fungsi untuk menghitung total pembayaran produk dengan diskon."""
  harga_diskon = produk.hitung_diskon(diskon)
  total = harga_diskon + 5000  
  return total

produk1 = Elektronik("Laptop", 6000000, 12)
produk2 = Fashion("Baju", 200000, "L")

diskon = 0.1  

total_1 = hitung_total(produk1, diskon)
total_2 = hitung_total(produk2, diskon)

print(f"Total pembayaran Laptop: Rp{total_1:,}")
print(f"Total pembayaran Baju: Rp{total_2:,}")