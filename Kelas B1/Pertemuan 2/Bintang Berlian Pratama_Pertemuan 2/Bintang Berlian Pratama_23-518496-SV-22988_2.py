class Karyawan:
    def __init__(self, Nama, Umur, Posisi):
        self.Nama = Nama
        self.Umur = Umur
        self.Posisi = Posisi
    def display(self):
        print("Nama:",self.Nama)
        print("Umur:",self.Umur)
        print("Posisi:",self.Posisi)

Karyawan1 = Karyawan("Mahmodin",30,"IT Staff")
Karyawan1.display()
