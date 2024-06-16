class manusia():
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def cetak(self):
        print(f"Namanya adalah {self.nama}")
        print(f"Umurnya {self.umur} tahun")


nama = input("Nama: ")
umur = int(input("Umur: "))

manusia1 = manusia(nama, umur)

manusia1.cetak()