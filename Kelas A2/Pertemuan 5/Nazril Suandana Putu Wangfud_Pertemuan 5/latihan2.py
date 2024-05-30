    # Definisikan kelas dasar (base class)
class OperasiMatematika:
        def hitung(self, a, b):
            pass

    # Definisikan kelas turunan (subclass) dari kelas OperasiMatematika
class Penjumlahan(OperasiMatematika):
        def hitung(self, a, b):
            return a + b

class Pengurangan(OperasiMatematika):
        def hitung(self, a, b):
            return a - b

class Perkalian(OperasiMatematika):
        def hitung(self, a, b):
            return a * b

class Pembagian(OperasiMatematika):
        def hitung(self, a, b):
            return a / b

    # Membuat objek dari kelas-kelas turunan
penjumlahan = Penjumlahan()
pengurangan = Pengurangan()
perkalian = Perkalian()
pembagian = Pembagian()

    # Memanggil method hitung pada kelas-kelas turunan
print(penjumlahan.hitung(3, 5))  
print(pengurangan.hitung(10, 4))  
print(perkalian.hitung(4, 6))  
print(pembagian.hitung(12, 2))  