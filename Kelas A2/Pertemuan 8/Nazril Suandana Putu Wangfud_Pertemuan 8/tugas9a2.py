class Planet:
    def __init__(self, nama, diameter):
        self.nama = nama
        self.diameter = diameter

    @classmethod
    def from_csv(cls, string):
        nama, diameter = string.split(',')
        return cls(nama.strip(), float(diameter.strip()))

    @staticmethod
    def keliling_lingkaran(diameter):
        return 3.14 * diameter

    @property
    def diameter_km(self):
        return self.diameter

    @property
    def diameter_m(self):
        return self.diameter * 1000

# Membuat objek Planet menggunakan metode class
merkurius = Planet.from_csv("Merkurius, 4879")
bumi = Planet.from_csv("Bumi, 12742")

# Menggunakan metode statik untuk menghitung keliling lingkaran
print("Keliling Merkurius:", Planet.keliling_lingkaran(merkurius.diameter))
# Menggunakan properti untuk mendapatkan diameter dalam kilometer dan meter
print("Diameter Bumi (km):", bumi.diameter_km)
print("Diameter Bumi (m):", bumi.diameter_m)