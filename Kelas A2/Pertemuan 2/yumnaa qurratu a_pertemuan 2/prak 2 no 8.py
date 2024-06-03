class Person:
    def __init__(self, nama, umur, pekerjaan):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")
        print(f"Pekerjaan: {self.pekerjaan}")

orang_pertama = Person(nama="John Doe", umur=30, pekerjaan="Insinyur")

orang_pertama.tampilkan_info()
print()
