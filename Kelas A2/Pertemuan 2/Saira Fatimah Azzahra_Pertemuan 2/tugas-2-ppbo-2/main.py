class Negara:
    def __init__ (self, nama, ibu_kota, populasi):
        self.nama = nama
        self.ibu_kota = ibu_kota
    
    def informasi_negara(self):
        print("Negara:", self.nama)
        print("Ibu Kota:", self.ibu_kota)
    
# Membuat objek-objek Negara
indonesia = Negara("Indonesia", "Nusantara")
jepang = Negara("Jepang", "Tokyo")
india = Negara("India", "New Delhi")
china = Negara("China", "Beijing")

# Menampilkan informasi tentang negara-negara
indonesia.informasi_negara()
jepang.informasi_negara()
india.informasi_negara()
china.informasi_negara()