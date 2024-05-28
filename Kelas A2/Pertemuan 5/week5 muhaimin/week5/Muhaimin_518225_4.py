class Bilangan:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        if isinstance(other, Bilangan):
            # Jika other adalah objek Bilangan, tambahkan nilai keduanya
            return Bilangan(self.nilai + other.nilai)
        elif isinstance(other, (int, float)):
            # Jika other adalah int atau float, tambahkan dengan nilai objek Bilangan
            return Bilangan(self.nilai + other)
        else:
            # Return None jika other tidak sesuai
            return None

    def __str__(self):
        return str(self.nilai)

# Membuat objek Bilangan
bilangan1 = Bilangan(5)
bilangan2 = Bilangan(10)

# Menggunakan operator overloading untuk penjumlahan
hasil_penjumlahan = bilangan1 + bilangan2
print("Hasil Penjumlahan:", hasil_penjumlahan)

# Juga dapat menggunakan operator overloading dengan tipe data lain
hasil_penjumlahan_int = bilangan1 + 3
print("Hasil Penjumlahan (int):", hasil_penjumlahan_int)

hasil_penjumlahan_float = bilangan2 + 7.5
print("Hasil Penjumlahan (float):", hasil_penjumlahan_float)
