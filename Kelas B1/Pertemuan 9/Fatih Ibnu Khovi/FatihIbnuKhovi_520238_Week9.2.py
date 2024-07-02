class Kopi:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga
    
    @property
    def nama(self):
        return self._nama
    
    @property
    def harga(self):
        return self._harga
    
    @classmethod
    def from_string(cls, string):
        nama, harga = string.split(',')
        return cls(nama.strip(), float(harga.strip()))
    
    @staticmethod
    def make_coffee(nama_kopi):
        return f"Membuat {nama_kopi}..."

arabika = Kopi("Arabika", 25000)
print("Nama kopi:", arabika.nama)
print("Harga kopi:", arabika.harga)

robusta = Kopi.from_string("Robusta, 30000")
print("Nama kopi:", robusta.nama)
print("Harga kopi:", robusta.harga)

print(Kopi.make_coffee("Espresso"))