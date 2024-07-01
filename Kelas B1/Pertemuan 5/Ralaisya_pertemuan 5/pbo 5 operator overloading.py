class Bilangan:
    def __init__(self, nilai):
        self.nilai = nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __sub__(self, other):
        return self.nilai - other.nilai

    def __mul__(self, other):
        return self.nilai * other.nilai

    def __str__(self):
        return str(self.nilai)

def main():
    bilangan1 = Bilangan(5)
    bilangan2 = Bilangan(3)

    hasil_penjumlahan = bilangan1 + bilangan2
    print("Hasil penjumlahan:", hasil_penjumlahan)

    hasil_pengurangan = bilangan1 - bilangan2
    print("Hasil pengurangan:", hasil_pengurangan)

    hasil_perkalian = bilangan1 * bilangan2
    print("Hasil perkalian:", hasil_perkalian)

if __name__ == "__main__":
    main()
