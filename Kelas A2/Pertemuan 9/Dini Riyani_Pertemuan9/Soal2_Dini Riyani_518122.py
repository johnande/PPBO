class Kecepatan:
    def __init__(self, jarak, waktu):
        self.jarak = jarak
        self.waktu = waktu

    @classmethod
    def dari_jarak_dan_waktu(cls, jarak, waktu):
        return cls(jarak, waktu)

    @staticmethod
    def hitung_kecepatan(jarak, waktu):
        return jarak / waktu

    @property
    def kecepatan(self):
        return self.jarak / self.waktu

    def tampilkan_info(self):
        print(f"Jarak: {self.jarak} km")
        print(f"Waktu tempuh: {self.waktu} jam")
        print(f"Kecepatan: {self.kecepatan} km/jam")


# Main program
jarak = float(input("Masukkan jarak (km): "))
waktu = float(input("Masukkan waktu tempuh (jam): "))

kecepatan = Kecepatan.dari_jarak_dan_waktu(jarak, waktu)

print("\nMenggunakan @classmethod:")
kecepatan.tampilkan_info()

print("\nMenggunakan @staticmethod:")
print("Kecepatan:", Kecepatan.hitung_kecepatan(jarak, waktu), "km/jam")

print("\nMenggunakan @property:")
print("Kecepatan:", kecepatan.kecepatan, "km/jam")
