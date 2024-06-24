class Buah:
    def __init__(self, nama):
        self.nama = nama

    def rasa(self):
        pass

class Apel(Buah):
    def rasa(self):
        return "Manis dan sedikit asam"

class Jeruk(Buah):
    def rasa(self):
        return "Segar dan asam"

class Pisang(Buah):
    def rasa(self):
        return "Manis dan lembut"

def tampilkan_rasa(buah):
    print(f"Buah {buah.nama}, Rasanya {buah.rasa()}")

buah1 = Apel("Apel")
buah2 = Jeruk("Jeruk")
buah3 = Pisang("Pisang")

tampilkan_rasa(buah1)
tampilkan_rasa(buah2)
tampilkan_rasa(buah3)
