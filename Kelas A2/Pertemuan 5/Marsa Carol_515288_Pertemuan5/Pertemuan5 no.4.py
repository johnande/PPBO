class Bilangan:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return self.nilai + other

# Membuat objek Bilangan
bilangan1 = Bilangan(5)

# Melakukan operasi penjumlahan dengan objek Bilangan dan bilangan bulat
hasil = bilangan1 + 10
print("Hasil penjumlahan:", hasil)

