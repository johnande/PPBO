class manusia:
    def __init__ (self, nama, umur):
        self.nama = nama
        self.umur = umur 

    def tampilkan_data_manusia(self):
        print("nama : " + self.nama)
        print("umur : " + str(self.umur))

manusia1=manusia("isa", "22")
manusia2=manusia("imin", "23")

manusia1.tampilkan_data_manusia()
manusia2.tampilkan_data_manusia()