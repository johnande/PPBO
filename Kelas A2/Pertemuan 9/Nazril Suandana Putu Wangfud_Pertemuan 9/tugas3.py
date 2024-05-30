class PlanetFactory:
    def create_planet(self, nama, massa, radius):
        return Planet(nama, massa, radius)

class Planet:
    def __init__(self, nama, massa, radius):
        self.nama = nama
        self.massa = massa
        self.radius = radius

    def get_nama(self):
        return self.nama

    def get_massa(self):
        return self.massa

    def get_radius(self):
        return self.radius

# Membuat factory
factory = PlanetFactory()

# Membuat objek planet menggunakan factory
earth = factory.create_planet("Bumi", 5.9999, 6.2222)
mars = factory.create_planet("Mars", 6.8888, 3.3333)

# Mengakses atribut objek planet
print("nama planet =",earth.get_nama())  # Output: BUmi
print("massa planet =",earth.get_massa())  # Output: 5.9999
print("radius planet =",earth.get_radius())  # Output: 6.2222
print("================================")
print("nama planet =", mars.get_nama())  # Output: Mars
print("massa planet =",mars.get_massa())  # Output: 6.42e23
print("radius planet =",mars.get_radius())  # Output: 3.39e6