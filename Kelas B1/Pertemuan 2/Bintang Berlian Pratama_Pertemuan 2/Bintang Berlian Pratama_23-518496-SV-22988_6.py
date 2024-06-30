class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def display(self):
        print("Nama:",self.nama)
        print("Umur:",self.umur)

Manusia1 = Manusia(input("Masukkan Nama: "),
                   int(input("Masukkan Umur: ")))
Manusia1.display()
