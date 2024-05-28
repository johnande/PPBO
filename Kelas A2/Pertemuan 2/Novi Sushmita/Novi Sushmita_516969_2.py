#membuat class
class luas_rumah:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar
    def tampilkan(self):
        print("Luas rumah: " + str(self.luas()))

#membuat object
rumah1 = luas_rumah(3, 4)
rumah1.tampilkan()

rumah2 = luas_rumah(9,5)
rumah2.tampilkan()