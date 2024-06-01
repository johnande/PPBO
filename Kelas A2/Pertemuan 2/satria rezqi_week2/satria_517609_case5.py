class manusia:

    def __init__(self, nama, umur) -> None:
        self.name = nama
        self.age = umur

    def cetakInfo (self):
        print(f'Nama:\t {self.name} \nUmur:\t {self.age}')

nama = input('Masukkan nama: ')
umur = input("masukkan umur: ")

manusia(nama, umur).cetakInfo()

