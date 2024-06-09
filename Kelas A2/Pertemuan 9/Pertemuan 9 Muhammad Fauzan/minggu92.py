class Lingkaran:
    _pi = 3.14159

    def __init__(self, radius):
        self._radius = radius

    @classmethod
    def buat_dari_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def hitung_luas(radius):
        return Lingkaran._pi * radius ** 2

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

# Contoh penggunaan
# Membuat instance menggunakan class method
lingkaran1 = Lingkaran.buat_dari_diameter(10)
print("Radius lingkaran1:", lingkaran1.radius)
print("Diameter lingkaran1:", lingkaran1.diameter)

# Menghitung luas lingkaran menggunakan static method
luas_lingkaran1 = Lingkaran.hitung_luas(lingkaran1.radius)
print("Luas lingkaran1:", luas_lingkaran1)
