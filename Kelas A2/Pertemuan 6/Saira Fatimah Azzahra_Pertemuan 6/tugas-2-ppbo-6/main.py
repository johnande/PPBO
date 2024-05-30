from abc import ABC, abstractmethod

class Mobil_Mewah(ABC):
    @abstractmethod
    def harga(self):
        pass
    
class Tesla(Mobil_Mewah):
    def harga(self):
        print("Harga mobil tesla 2 miliar rupiah")

class Lexus(Mobil_Mewah):
    def harga(self):
        print("Harga mobil lexus 3 miliar rupiah")
        
class Ferrari(Mobil_Mewah):
    def harga(self):
        print("Harga mobil ferrari 10 miliar rupiah")
        
tesla = Tesla()
tesla.harga()

lexus = Lexus()
lexus.harga()

ferrari = Ferrari()
ferrari.harga()