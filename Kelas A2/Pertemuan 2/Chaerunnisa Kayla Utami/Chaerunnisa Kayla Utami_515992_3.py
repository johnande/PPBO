class Persegi:
  def __init__(self, sisi):
    self.sisi = sisi

  def luas(self):
    return self.sisi ** 2

  def keliling(self):
    return 4 * self.sisi

# Membuat objek persegi
persegi1 = Persegi(5)

# Menghitung luas dan keliling
luas = persegi1.luas()
keliling = persegi1.keliling()

# Menampilkan hasil
print(f"Luas persegi dengan sisi {persegi1.sisi} cm adalah {luas} cm^2")
print(f"Keliling persegi dengan sisi {persegi1.sisi} cm adalah {keliling} cm")
