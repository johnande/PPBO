from abc import ABC, abstractmethod

# Abstract class untuk minuman
class Minuman(ABC):
    @abstractmethod
    def deskripsi(self):
        pass

# Concrete class untuk kopi
class Kopi(Minuman):
    def deskripsi(self):
        return "Ini adalah segelas kopi."

# Concrete class untuk teh
class Teh(Minuman):
    def deskripsi(self):
        return "Ini adalah segelas teh."

# Factory class untuk membuat minuman
class PabrikMinuman:
    @staticmethod
    def pesan_minuman(jenis):
        if jenis.lower() == 'kopi':
            return Kopi()
        elif jenis.lower() == 'teh':
            return Teh()
        else:
            raise ValueError("Jenis minuman tidak valid.")

# Fungsi utama
def main():
    jenis_minuman = input("Apa yang ingin Anda pesan? (Kopi/Teh): ")
    minuman = PabrikMinuman.pesan_minuman(jenis_minuman) 
    print(minuman.deskripsi())
   

if __name__ == "__main__":
    main()
