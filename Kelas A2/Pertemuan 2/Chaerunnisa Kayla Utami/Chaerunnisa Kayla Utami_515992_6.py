class Manusia:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def perkenalan(self):
    print(f"Halo, nama saya {self.nama} dan saya berusia {self.umur} tahun.")

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))

manusia1 = Manusia(nama, umur)
manusia1.perkenalan()
