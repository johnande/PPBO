class Sepatu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __lt__(self, lain):
        return self.harga < lain.harga

NikeDunk = Sepatu("NikeDunk", 1999)
AdidasSamba = Sepatu("Adidas Samba", 1200)

if NikeDunk < AdidasSamba:
    print (f"{NikeDunk.nama} lebih murah dari {AdidasSamba.nama}")
else :
    print (f"{NikeDunk.nama} lebih mahal dari {AdidasSamba.nama}")