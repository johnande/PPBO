# Definisi kelas dekorator
def tambah_rasa(rasa):
    def decorator(cls):
        class DecoratedFruit(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.rasa = rasa
        return DecoratedFruit
    return decorator

# Kelas dasar Buah
class Buah:
    def __init__(self, nama):
        self.nama = nama

# Mendekorasi kelas Buah dengan dekorator tambah_rasa
@tambah_rasa("manis")
class BuahDenganRasa(Buah):
    pass

# Membuat objek buah dan mencetak nama dan rasa
buah1 = BuahDenganRasa("Apel")
print(f"Buah: {buah1.nama}, Rasa: {buah1.rasa}")
