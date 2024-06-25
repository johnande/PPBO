#No8

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def info(self):
        print(f"Mahasiswa {self.nama} dengan NIM {self.nim}")

mhs1 = Mahasiswa("Nayla Kamalati", "521253")
mhs1.info()