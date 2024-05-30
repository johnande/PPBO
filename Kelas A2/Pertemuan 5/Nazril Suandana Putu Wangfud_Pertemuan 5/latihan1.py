# Definisikan kelas induk
class Hewan:
    def suara(self):
        pass

# Definisikan kelas turunan
class Anjing(Hewan):
    def suara(self):
        return "Guk Guk"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

# Buat objek dari kelas turunan
anjing = Anjing()
kucing = Kucing()

# Panggil method suara pada kedua objek
print("Anjing menggonggong :",anjing.suara())  # Output: Guk Guk
print("kucing mengeong :",kucing.suara())  # Output: Meow