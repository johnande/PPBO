class manusia:
    def __init__ (self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampil(self):
        print("Nama Anda: " + self.nama)
        print("Umur Anda: " + str(self.umur))
        
manusia1 = manusia(input("nama : "), input("umur : "))
manusia1.tampil()