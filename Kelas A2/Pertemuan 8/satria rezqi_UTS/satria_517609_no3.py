from abc import ABC, abstractmethod

#kelas abc
class Spesificationn(ABC):
    @abstractmethod
    def show_chase(self):
        pass

    @abstractmethod
    def superiority(self):
        pass

#kelas ini merupakan turunan dari kelas ABC yang akan menjadi parent class dari kelas merk mobil lainnya
class Car(Spesificationn):
    def __init__(self, series, merk, engine, fuelTank, maxSpeed) -> None:
        self.series = series
        self.merk = merk
        self.engine = engine
        self.fuelTank = fuelTank
        self.maxSpeed = maxSpeed

    def show_chase(self):
        data = """SPESIFICATION:
        --> Series\t: {}
        --> Merk\t: {}
        --> Engine\t: {} cc
        --> Fuel Tank\t: {} Liter
        --> Max Speed\t: {} km/h""".format(self.series, self.merk, self.engine, self.fuelTank, self.maxSpeed)

        return data

#kelas Honda merupakan kelas turunan dari kelas Car, dimana kelas ini akan mewarisi konstruktor, method show_chase dan superiority dari kelas Car
class Honda(Car):
    #method superiority ini akan mengembalikan data yang berisi kelebihan dari mobil Honda, disinilah konsep polymorphism terjadi
    def superiority(self):
        data = """HONDA SUPERIORITY:
        --> Honda is a car with a good engine
        --> Honda has a large fuel tank
        --> Honda has a high speed
        --> This brand is very popular in the world
        --> Honda has so many car categories, such as SUV car, sedan car, and even they have a sport car"""
        return data
    
class Lamborghini(Car):
    #dengan konsep polimorphism, method superiority yang ada pada kelas Honda dan Lamborghini akan mengeluarkan output yang berbeda.
    def superiority(self):
        data = """LAMBORGHINI SUPERIORITY:
        --> Lamborghini is a brand of car with focusing on sports car
        --> Lamborghini car always use high engine capacity
        --> This car has sports design, make it look more luxurious
        --> Because of it's engine, this car has high speed"""
        return data
    
#inisialisasi objek
aventador = Lamborghini("Aventador", "Lamborghini", 6500, 90, 350)
print(aventador.show_chase())
print(aventador.superiority())
print()
jazz = Honda("Jazz", "Honda", 1500, 40, 200)
print(jazz.show_chase())
print(jazz.superiority())