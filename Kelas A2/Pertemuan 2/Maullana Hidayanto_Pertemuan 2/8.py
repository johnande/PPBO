class Pemain :
    def __init__ (self, Nama, Nomor):
        self.Nama = Nama
        self.Nomor = Nomor

    def tampilkan_data(self):
        print("Nama : " + self.Nama)
        print("Nomor : " + str(self.Nomor))

pemain1 = Pemain("Mudrik", 15)
pemain2 = Pemain("Komeng", 10)

pemain1.tampilkan_data()
pemain2.tampilkan_data()