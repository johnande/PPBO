class Makanan:
    def __init__(self, nama):
        self.nama = nama

    def deskripsi(self):
        return f"Deskripsi makanan belum diimplementasikan."

class Pizza(Makanan):
    def deskripsi(self):
        return f"{self.nama} adalah makanan yang terbuat dari adonan, saus, dan berbagai topping."

class Burger(Makanan):
    def deskripsi(self):
        return f"{self.nama} adalah makanan yang terdiri dari roti, patty, saus, dan sayuran."

class Pasta(Makanan):
    def deskripsi(self):
        return f"{self.nama} adalah makanan yang terbuat dari pasta yang dimasak dengan berbagai saus."

def main():
    makanan1 = Pizza("Pizza Margherita")
    makanan2 = Burger("Cheeseburger")
    makanan3 = Pasta("Spaghetti Bolognese")

    print(makanan1.deskripsi())
    print(makanan2.deskripsi())
    print(makanan3.deskripsi())

    makanan_generic = Makanan("Makanan Umum")
    print(makanan_generic.deskripsi())

if __name__ == "__main__":
    main()
