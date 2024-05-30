class Buah:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    
    @property
    def info(self):
        return f"{self.nama} adalah jenis buah {self.jenis}."
    
    @classmethod
    def monokotil(cls, nama):
        return cls(nama, 'monokotil')
    
    @classmethod
    def dikotil(cls, nama):
        return cls(nama, 'dikotil')
    
    @staticmethod
    def ciri_ciri_monokotil():
        return "Buah-buahan monokotil memiliki biji tunggal."

    @staticmethod
    def ciri_ciri_dikotil():
        return "Buah-buahan dikotil memiliki biji lebih dari satu."
        

# Contoh penggunaan
buah1 = Buah.monokotil("Padi")
print(buah1.info)  # Output: pisang adalah jenis buah monokotil.
print(Buah.ciri_ciri_monokotil())  # Output: Buah-buahan monokotil memiliki biji tunggal.
print()

buah2 = Buah.dikotil("Apel")
print(buah2.info)  # Output: apel adalah jenis buah dikotil.
print(Buah.ciri_ciri_dikotil())  # Output: Buah-buahan dikotil memiliki biji lebih dari satu.
