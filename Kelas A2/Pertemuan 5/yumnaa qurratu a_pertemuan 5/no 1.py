class Novel:
    def genre(self):
        print("Fiksi")
        
    def jumlah_halaman(self):
        print("Jumlah halaman rata-rata: 400")
        
class BukuDongeng:
    def genre(self):
        print("Fiksi")
        
    def jumlah_halaman(self):
        print("Jumlah halaman rata-rata: 30")
        
novel = Novel()
buku_dongeng = BukuDongeng()

#iterate objects of same type
for buku in (novel, buku_dongeng):
    #call methods without checking class of object
    buku.genre()
    buku.jumlah_halaman()
