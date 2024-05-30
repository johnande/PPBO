class Angka:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        if isinstance(other, Angka):
            return Angka(self.nilai + other.nilai)
        else:
            raise ValueError("Operasi tidak mendukung. Objek harus merupakan instance dari Angka.")

# Membuat objek Angka
angka1 = Angka(5)
angka2 = Angka(2)

# Menggabungkan dua angka menggunakan operator overloading '+'
hasil_penjumlahan = angka1 + angka2

# Menampilkan hasil penjumlahan
print(f"Hasil penjumlahan:" ,hasil_penjumlahan.nilai)
