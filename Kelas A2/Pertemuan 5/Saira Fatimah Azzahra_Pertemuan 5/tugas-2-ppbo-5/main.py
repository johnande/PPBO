import math

class Bentuk:
    def area(self):
        pass

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def area(self):
        return self.panjang * self.lebar

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def area(self):
        return 0.5 * self.alas * self.tinggi

def main():
    bentuk1 = PersegiPanjang(5, 4)
    bentuk2 = Lingkaran(3)
    bentuk3 = Segitiga(6, 4)

    print("Luas Persegi Panjang:", bentuk1.area())
    print("Luas Lingkaran:", bentuk2.area())
    print("Luas Segitiga:", bentuk3.area())

if __name__ == "__main__":
    main()