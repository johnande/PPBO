class Manusia:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tampilkan(self):
        print("Nama:", self.name)
        print("Umur:", self.age)

name = input("Masukkan nama: ")
age = int(input("Masukkan umur: "))

orang = Manusia(name, age)
orang.tampilkan()