class Manusia:
    def __init__(self, nama, umur):
      self.nama = nama
      self.umur = umur

    def tampilkan_data(self):
      print("\nInformasi tentang manusia:")
      print("Nama:", self.nama)
      print("Umur:", self.umur)

nama_input = input("Masukkan nama: ")
umur_input = input("Masukkan umur: ")
manusia1 = Manusia(nama_input, umur_input)
manusia1.tampilkan_data()
