class Manusia:
    def __init__ (self, nama, umur):
        self.nama = nama
        self.umur = umur

    def informasi(self):
        print("\nNama:", self.nama)
        print("Umur:", self.umur)

nama = input("Masukkan nama :")
umur = int(input("Masukkan Umur:"))

manusia = Manusia(nama, umur)

manusia.informasi()